import threading
import time
import src.functions as f


# Main Function
def main():
    f.initialize_display()
    
    # Create sensor threads
    sensor_threads = [threading.Thread(target=f.simulate_sensor, args=(i,), daemon=True) for i in range(3)]
    for thread in sensor_threads:
        thread.start()
    
    # Create processing thread
    processing_thread = threading.Thread(target=f.process_temperatures, daemon=True)
    processing_thread.start()
    
    # Create display update thread
    display_thread = threading.Thread(target=f.update_display, daemon=True)
    display_thread.start()
    
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
