import src.sequential as seq
import src.threading as th
import src.processes as pr
import src.dataprocessing as dp
import multiprocessing

X_train_filled, X_val_filled, y_train, y_val = dp.prepare()

sequential_time = seq.execution(X_train_filled, X_val_filled, y_train, y_val)
threading_time = th.execution(X_train_filled, X_val_filled, y_train, y_val)
processing_time = pr.execution(X_train_filled, X_val_filled, y_train, y_val)

cpu = multiprocessing.cpu_count()

s_threading = sequential_time / threading_time
print(f"Threading Speedup: {s_threading}.")

s_processes = sequential_time / processing_time
print(f"Multiprocessing Speedup: {s_processes}.")

e_threading = s_threading / cpu
print(f"Threading Efficiency: {e_threading}.")

e_processes = s_processes / cpu
print(f"Multiprocessing Efficiency: {e_processes}.")

parallel_portion = 1 - ((sequential_time / processing_time) / sequential_time)

amdahl = 1 / ((1 - parallel_portion) + (parallel_portion / cpu))
print(f"Amdahl's: '{amdahl}.")

gustafsson = (1 - parallel_portion) + (parallel_portion * cpu)
print(f"Gustafsson's: {gustafsson}.")