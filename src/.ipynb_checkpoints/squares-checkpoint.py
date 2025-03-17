import multiprocessing
from src.sequential import sequential_processing
from src.processing import multiprocessing_pool_map, multiprocessing_pool_apply, process_pool_executor

def execution():
    numbers = list(range(10**6))
    seq_time = sequential_processing(numbers)
    pool_map_time = multiprocessing_pool_map(numbers)
    pool_apply_time = multiprocessing_pool_apply(numbers)
    executor_time = process_pool_executor(numbers)
    
    # Compute Speedup, Efficiency, Amdahl's Law, and Gustafson's Law
    def compute_metrics(seq_time, parallel_time, num_processors):
        speedup = seq_time / parallel_time
        efficiency = speedup / num_processors
        amdahl = 1 / ((1 - (1 / speedup)) + (1 / num_processors))
        gustafson = num_processors - (1 - speedup)
        return speedup, efficiency, amdahl, gustafson
    
    num_processors = multiprocessing.cpu_count()
    
    for method, time_taken in zip([
        "Multiprocessing Pool (map)",
        "Multiprocessing Pool (apply)",
        "ProcessPoolExecutor"],
        [pool_map_time, pool_apply_time, executor_time]):
        speedup, efficiency, amdahl, gustafson = compute_metrics(seq_time, time_taken, num_processors)
        print(f"\n{method}:")
        print(f"Speedup: {speedup:.4f}")
        print(f"Efficiency: {efficiency:.4f}")
        print(f"Amdahl's Law Speedup: {amdahl:.4f}")
        print(f"Gustafson's Law Speedup: {gustafson:.4f}")
