import src.sequential as seq
import src.threading as th
import src.processes as pr

chars = 1000000
threads_n = 8
processes_n = 8

sequential_t = seq.testing(chars)
threading_t = th.testing(chars, threads_n)
processing_t = pr.testing(chars, processes_n)

# Calculate speedups
speedup_threading = sequential_t / threading_t
speedup_processing = sequential_t / processing_t

# Calculate efficiency
efficiency_threading = speedup_threading / threads_n
efficiency_processing = speedup_processing / processes_n

# Calculate Ahmdahl's
ahmdahls_threading = 1 / ((1 - 0.54) + (0.54 / threads_n))
ahmdahls_processing = 1 / ((1 - 0.54) + (0.54 / processes_n))

# Calculate Gustafsson's
gustafssons_threading = threads_n / ((1 - 0.54) + (0.54 / threads_n))
gustafssons_processing = processes_n / ((1 - 0.54) + (0.54 / processes_n))

print("------------------------------------------------------------------")
print(f"Speedup (Threading): {speedup_threading}")
print(f"Speedup (Multiprocessing): {speedup_processing}")
print("------------------------------------------------------------------")
print(f"Efficiency (Threading): {efficiency_threading}")
print(f"Efficiency (Multiprocessing): {efficiency_processing}")
print("------------------------------------------------------------------")
print(f"Ahmdahl's (Threading): {ahmdahls_threading}")
print(f"Ahmdahl's (Multiprocessing): {ahmdahls_processing}")
print("------------------------------------------------------------------")
print(f"Gustafsson's (Threading): {gustafssons_threading}")
print(f"Gustafsson's (Multiprocessing): {gustafssons_processing}")