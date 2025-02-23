import random
import time

latest_temperatures = {}
temperature_averages = {}

def simulate_sensor(sensor):
    while True:
        temp = random.randint(15, 40)
        
        latest_temperatures[sensor] = temp
        
        temperature_queue.append(temp)
        
        time.sleep(1)

def process_temperatures():
    if temperature_queue:
        avg_temp = sum(temperature_queue) / len(temperature_queue)
        temperature_averages[sensor] = avg_temp
        
        time.sleep(1)