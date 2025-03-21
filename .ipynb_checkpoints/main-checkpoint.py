from mpi4py import MPI
from src.genetic_algorithm_trial import execution as sequential
from src.genetic_algorithm_parallel import genetic_algorithm_mpi
from src.genetic_algorithm_extended import genetic_algorithm_extended

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()  # Get the number of processes

# --- Sequential run (only on rank 0) ---
if rank == 0:
    sequential_time = sequential()
    print(f"\nSequential Execution Time: {sequential_time:.4f} seconds")

# --- Parallel GA run ---
comm.Barrier()  # Synchronize all ranks
parallel_time = genetic_algorithm_mpi()
# parallel_total_time = comm.reduce(parallel_time, op=MPI.MAX, root=0)

# --- Extended GA run ---
# comm.Barrier()
# extended_time = genetic_algorithm_extended()
# extended_total_time = comm.reduce(extended_time, op=MPI.MAX, root=0)

# Compute performance metrics on rank 0
if rank == 0:
    # Speedup (S)
    speedup = sequential_time / parallel_time
    print(f"Speedup (S): {speedup:.2f}")

    # Efficiency (E)
    efficiency = speedup / size
    print(f"Efficiency (E): {efficiency:.2%}")

    # Amdahl's Law: S = 1 / ( (1 - P) + P / N )
    P = 0.9  # Assumption: 90% of execution is parallelizable (adjust based on profiling)
    amdahl_speedup = 1 / ((1 - P) + (P / size))
    print(f"Amdahl’s Law Speedup: {amdahl_speedup:.2f}")

    # Gustafson’s Law: S = N - α(N - 1)
    alpha = 1 - P  # Sequential portion
    gustafson_speedup = size - alpha * (size - 1)
    print(f"Gustafson’s Law Speedup: {gustafson_speedup:.2f}")

    print(f"Parallel Execution Time: {parallel_time}")
