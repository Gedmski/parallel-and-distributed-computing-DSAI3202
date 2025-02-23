import threading

for i in range(3)
    sensor_thread = threading.Thread(target=simulate_sensor, daemon=True)
    processing_thread = threading.Thread(target=process_temperatures, daemon=True)
    
    sensor_thread.start()
    processing_thread.start()