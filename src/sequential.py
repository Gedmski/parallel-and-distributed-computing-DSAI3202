import time
import src.functions as f

def testing(chars):
    # Measure the total time for both operations
    total_start_time = time.time()
    
    # Run the functions
    joined_letters = f.join_random_letters(chars)
    total_sum = f.add_random_numbers(chars)
    
    total_end_time = time.time()

    # Print the results
    print("----- Sequential Results -----")
    print(f"Total time taken: {total_end_time - total_start_time} seconds")
    return total_end_time - total_start_time