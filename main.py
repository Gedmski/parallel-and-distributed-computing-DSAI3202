from mpi4py import MPI
import numpy as np
from src.square import square
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

results = None

if rank == 0:
    numbers = np.arange(size, dtype="i")
else:
    numbers = None

number = np.zeros(1, dtype="i")
comm.Scatter(numbers, number, root=0)

result = square(number[0])

time.sleep(random.randint(1,11))
request = comm.isend(result, dest=0, tag=rank)
print(result)

if rank == 0:
    results = np.zeros(size, dtype="i")
    for i in range(size):
        results[i] = comm.irecv(source=i, tag=i).wait()
    print(f"The results are: {results}")
    
request.wait()