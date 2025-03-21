import threading
import random
import time
import queue
import sys
import os

latest_temperatures = {}
temperature_averages = {}
temp_queue = queue.Queue()
lock = threading.RLock()
condition = threading.Condition(lock)

# Sensor Simulation
def simulate_sensor(sensor_id):
    """
    Simulates a temperature sensor that generates a random temperature
    reading between 15°C and 40°C every second.

    Parameters:
    - sensor_id (int): The ID of the sensor.

    Side Effects:
    - Updates the global `latest_temperatures` dictionary with the current reading.
    - Puts the reading into the `temp_queue` for processing.
    """
    global latest_temperatures
    while True:
        temp = random.randint(15, 40)
        with lock:
            latest_temperatures[sensor_id] = temp
            temp_queue.put((sensor_id, temp))
        time.sleep(1)

# Data Processing
def process_temperatures():
    """
    Continuously processes temperature readings from the queue to compute
    running averages for each sensor.

    Side Effects:
    - Updates the global `temperature_averages` dictionary with the calculated averages.
    - Waits using a condition variable when the queue is empty to avoid busy-waiting.
    """
    sensor_data = {}
    sensor_counts = {}
    while True:
        with condition:
            while temp_queue.empty():
                condition.wait()
            
            sensor_id, temp = temp_queue.get()
            if sensor_id not in sensor_data:
                sensor_data[sensor_id] = 0
                sensor_counts[sensor_id] = 0
            
            sensor_data[sensor_id] += temp
            sensor_counts[sensor_id] += 1
            temperature_averages[sensor_id] = round(sensor_data[sensor_id] / sensor_counts[sensor_id], 2)
        
        time.sleep(1)

# Display Logic
def initialize_display():
    """
    Prints the initial layout of the temperature monitoring display.

    This includes placeholders ("--") for the latest and average temperature
    values of all sensors.
    """
    print("Current temperatures:")
    print("Latest Temperatures:", end=" ")
    for i in range(3):
        print(f"Sensor {i}: --°C", end=" ")
    print()
    for i in range(3):
        print(f"Sensor {i} Average: --°C")

def update_display():
    """
    Periodically updates the temperature display in-place every 5 seconds.

    - Retrieves the latest and average temperatures for each sensor.
    - Clears the console and redraws the updated values without erasing the structure.
    """
    while True:
        time.sleep(5)
        with lock:
            print("\033[H\033[J", end="")  # Clears console screen
            print("\rCurrent temperatures:")
            print("Latest Temperatures:", end=" ")
            for i in range(3):
                temp = latest_temperatures.get(i, "--")
                print(f"Sensor {i}: {temp}°C", end=" ")
            print()
            for i in range(3):
                avg_temp = temperature_averages.get(i, "--")
                print(f"Sensor {i} Average: {avg_temp}°C")