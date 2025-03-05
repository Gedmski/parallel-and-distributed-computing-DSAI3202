import multiprocessing as mp
import src.sequential as seq
import src.parallel as par
import src.functions as funct
import src.extractions as extract

yes_images, no_images = funct.execution()

execution_time = seq.execution(yes_images, no_images)
execution_time_p, yes_inputs, no_inputs = par.execution(yes_images, no_images)

cpu = mp.cpu_count()

speedup = execution_time / execution_time_p
print(f"Multiprocessing Speedup: {speedup:.2f}.")

efficiency = speedup / cpu
print(f"Multiprocessing Efficiency: {efficiency:.2f}.")

parallel_portion = 1 - ((execution_time / execution_time_p) / execution_time)

amdahl = 1 / ((1 - parallel_portion) + (parallel_portion / cpu))
print(f"Amdahl's: {amdahl}.")

gustafson = (1 - parallel_portion) + (parallel_portion * cpu)
print(f"Gustafson's: {gustafson}.")

df = extract.execution(yes_inputs, no_inputs)