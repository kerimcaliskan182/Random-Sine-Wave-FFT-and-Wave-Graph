# Importing used libraries
import threading
import math
import random
import time
import socket
import matplotlib.pyplot as plt
from datetime import datetime
from queue import Queue
from matplotlib.animation import FuncAnimation
import numpy as np

# # Define the Samples Per Second for data collection (I adjusted to 10 because fewer data gives out better graph)
sps = 10

# Lists to store data for plotting
time_values = []  # Stores time values
sine_wave_values = []  # Stores sine wave values

# Fixed time window (in seconds) for the graph and initializing current time
time_window = 10
current_time = 0

# Define UDP settings
udp_host = "192.168.1.2"  # Replace with the target IP address
udp_port = 12345  # Choose an appropriate port number

# Queue for storing received data
max_queue_size = 500
data_queue = Queue(maxsize=max_queue_size)


def producer():
    while True:
        global current_time
        amplitude = random.randint(1, 10)  # Generate random amplitude value (between 1 and 10)
        frequency = random.randint(1, 10)  # Generate random frequency value (between 1 and 10)

        # To create the values for the sine wave
        sine_wave_value = amplitude * math.sin(2 * math.pi * frequency * current_time)

        # Send data via UDP socket
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.sendto(str(sine_wave_value).encode(), (udp_host, udp_port))
        udp_socket.close()

        time.sleep(1 / sps)  # Control the sample rate by introducing a sleep (With the sps we have it will give out
        # 10 data per second )


def consumer():
    global current_time  # Declare current_time as global to update it

    if data_queue.qsize() >= sps:
        print("Consuming data")
        for i in range(data_queue.qsize()):
            number = data_queue.get()

            # Update data arrays for plotting
            time_values.append(current_time)
            sine_wave_values.append(number)

            # Increasing the current time in each loop
            current_time += 1 / sps

    plt.cla()

    # Perform FFT on the received data if there are values
    if sine_wave_values:
        fft_values = np.fft.fft(sine_wave_values)
        fft_freq = np.fft.fftfreq(len(fft_values), 1 / sps)

        # Plot the FFT results
        plt.plot(fft_freq, np.abs(fft_values), label='FFT of Sine Wave')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude')
    plt.legend()


def udp_receiver():
    # To get the data from the UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", udp_port))

    while True:
        data, addr = udp_socket.recvfrom(1024)
        # Decoding sine wave values
        sine_wave_value = float(data.decode())

        # Append the current time and received sine wave value to the data lists
        time_values.append(current_time)
        sine_wave_values.append(sine_wave_value)
        data_queue.put(True)


def time_print():
    # The reason for this function is just print current time which has passed since the code has started
    while True:
        formatted_time = datetime.fromtimestamp(current_time).strftime('%S')
        print(f"Current time: {formatted_time}")
        time.sleep(1)


if __name__ == "__main__":
    # Create a producer thread that runs the producer() function
    producer_thread = threading.Thread(target=producer)
    producer_thread.start()

    # Create a UDP receiver thread that runs the udp_receiver() function
    udp_receiver_thread = threading.Thread(target=udp_receiver)
    udp_receiver_thread.start()

    # Create a time thread that runs the time_print() function
    time_thread = threading.Thread(target=time_print)
    time_thread.start()

    # Turn on interactive mode for Matplotlib
    plt.ion()

    # Create a figure and axis for plotting
    fig, ax = plt.subplots()

    while True:
        # Check if the data_queue is not empty, indicating new data received
        if not data_queue.empty():
            consumer()  # Call the consumer function to update the plot when data is received
        plt.pause(0.01)  # Update the plot every 10 milliseconds
