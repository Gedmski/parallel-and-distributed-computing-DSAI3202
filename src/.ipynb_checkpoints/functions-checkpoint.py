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
    global latest_temperatures
    while True:
        temp = random.randint(15, 40)
        with lock:
            latest_temperatures[sensor_id] = temp
            temp_queue.put((sensor_id, temp))
        time.sleep(1)

# Data Processing
def process_temperatures():
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
    print("Current temperatures:")
    print("Latest Temperatures:", end=" ")
    for i in range(3):
        print(f"Sensor {i}: --°C", end=" ")
    print()
    for i in range(3):
        print(f"Sensor {i} Average: --°C")

def update_display():
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