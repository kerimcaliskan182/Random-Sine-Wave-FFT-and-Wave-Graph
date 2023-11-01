Sine Wave Data Visualization and UDP Communication
This repository contains two Python scripts for generating and visualizing sine wave data and communicating it over UDP (User Datagram Protocol).

Script 1: sine_wave_code_FFTgraph.py
This script generates random sine wave data and visualizes it using an FFT (Fast Fourier Transform) graph. It also demonstrates UDP communication for data reception.

Key Components:
Sampling Rate (sps): The script allows you to define the Samples Per Second for data collection.

Data Storage: Lists are used to store time values and sine wave amplitude values for plotting.

Fixed Time Window: A fixed time window (in seconds) is set for the graph, and it initializes the current time.

UDP Configuration: You can specify the target IP address (udp_host) and port number (udp_port) for UDP communication.

Data Queue: Data received is stored in a queue (data_queue) for processing and plotting.

Producer Function: Generates random amplitude and frequency values to create the sine wave data. It sends the data via UDP socket.

Consumer Function: Updates the plot with the received data and performs FFT analysis. It ensures the data falls within the defined time window.

UDP Receiver Function: Listens for UDP packets, decodes received data, and stores it for visualization.

Time Print Function: Prints the current time elapsed since the script started.

Multithreading: Three separate threads are created for data generation, UDP communication, and time printing.

Matplotlib: The script uses Matplotlib for real-time visualization of sine wave data and its FFT analysis.

Script 2: sine_wave_code_sineGraph.py
This script focuses on generating random sine wave data and visualizing it using a traditional sine wave graph. It also demonstrates UDP communication for data reception.

Key Components:
Sampling Rate (sps): You can define the Samples Per Second for data collection in this script as well.

Time Window for Plotting: The script uses a time window (in seconds) to control the duration of the graph.

UDP Configuration: You specify the target IP address (udp_host) and port number (udp_port) for UDP communication.

Queue for Data Storage: Received data is stored in a queue for processing and plotting.

Producer Function: Generates random amplitude and frequency values, calculates the sine wave data, and sends it via UDP.

Consumer Function: Updates the sine wave plot with the received data, ensuring it falls within the defined time window.

UDP Receiver Function: Listens for UDP packets, decodes the data, and stores it for visualization.

Time Print Function: Prints the elapsed time since the script started.

Multithreading: Three threads are created for data generation, UDP communication, and time printing.

Matplotlib: Matplotlib is used for real-time visualization of the sine wave data.
