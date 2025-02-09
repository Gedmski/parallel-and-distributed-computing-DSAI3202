import threading
import time
import src.functions as f

def testing(chars, n_chunks):
    total_start_time = time.time()

    chunk = chars // n_chunks
    # Create threads for both functions
    threads = []
    for i in range(n_chunks):
        # thread_letters = threading.Thread(target=f.join_random_letters, args=(chunk,))
        thread_numbers = threading.Thread(target=f.add_random_numbers, args=(chunk*i, chunk*(i+1)))
        # threads.append(thread_letters)
        threads.append(thread_numbers)
        # thread_letters.start()
        thread_numbers.start()

        # Wait for all threads to complete
    for thread in threads:
        thread.join()

    total_end_time = time.time()
    print("----- Threading Results -----")
    print(f"Total time taken: {total_end_time - total_start_time} seconds")
    print("------------------------------------------------------------------")
    return total_end_time - total_start_time