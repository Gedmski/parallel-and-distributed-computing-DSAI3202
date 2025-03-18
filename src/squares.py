import multiprocessing
from src.sequential import sequential_processing
from src.processing import multiprocessing_for_loop, process_pool_executor, multiprocessing_pool_apply_sync, multiprocessing_pool_map_sync, multiprocessing_pool_apply_async, multiprocessing_pool_map_async

def execution():
    for size in [10**6, 10**7]:  # Testing both 10^6 and 10^7 numbers
        print(f"\nRunning tests with {size} numbers...\n")
        
        numbers = list(range(size))
        seq_time = sequential_processing(numbers)
        # mp_for_loop_time = multiprocessing_for_loop(numbers)
        print("Multiprocessing using for loop stopped due to too many processors.")
        executor_time = process_pool_executor(numbers)
        sync_apply_time = multiprocessing_pool_apply_sync(numbers)
        sync_map_time = multiprocessing_pool_map_sync(numbers)
        async_apply_time = multiprocessing_pool_apply_async(numbers)
        async_map_time = multiprocessing_pool_map_async(numbers)

        # Compute Speedup, Efficiency, Amdahl's Law, and Gustafson's Law
        def compute_metrics(seq_time, parallel_time, num_processors):
            speedup = seq_time / parallel_time
            efficiency = speedup / num_processors
            amdahl = 1 / ((1 - (1 / speedup)) + (1 / num_processors))
            gustafson = num_processors - (1 - speedup)
            return speedup, efficiency, amdahl, gustafson
        
        num_processors = multiprocessing.cpu_count()
        
        for method, time_taken in zip([
            "ProcessPoolExecutor",
            "Synchronous Pool (apply)",
            "Synchronous Pool (map)",
            "Asynchronous Pool (apply_async)",
            "Asynchronous Pool (map_async)"],
            [executor_time, 
             sync_apply_time, sync_map_time, async_apply_time, async_map_time]):
            speedup, efficiency, amdahl, gustafson = compute_metrics(seq_time, time_taken, num_processors)
            print(f"\n{method}:")
            print(f"Speedup: {speedup:.4f}")
            print(f"Efficiency: {efficiency:.4f}")
            print(f"Amdahl's Law Speedup: {amdahl:.4f}")
            print(f"Gustafson's Law Speedup: {gustafson:.4f}")
