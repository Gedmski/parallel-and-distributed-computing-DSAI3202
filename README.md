# Multiprocessing Performance Analysis
## Author
Gabriel Marquez

## Overview
This project evaluates the performance of different multiprocessing techniques in Python, analyzing their execution time, speedup, and efficiency. The tests compare sequential processing against:

- `multiprocessing.Pool(map)`
- `multiprocessing.Pool(apply)`
- `concurrent.futures.ProcessPoolExecutor`

## Part 1: Performance Analysis

### Initial Results
#### Execution Times:
- **Sequential processing:** `0.0712 seconds`
- **Multiprocessing Pool (map):** `0.1689 seconds`
- **Multiprocessing Pool (apply):** `164.6760 seconds`
- **ProcessPoolExecutor:** `107.7348 seconds`

#### Speedup and Efficiency:
| Method                           | Speedup | Efficiency | Amdahl's Law Speedup | Gustafson's Law Speedup |
| -------------------------------- | ------- | ---------- | -------------------- | ----------------------- |
| **Multiprocessing Pool (map)**   | 0.4215  | 0.0703     | -0.8295              | 5.4215                  |
| **Multiprocessing Pool (apply)** | 0.0004  | 0.0001     | -0.0004              | 5.0004                  |
| **ProcessPoolExecutor**          | 0.0007  | 0.0001     | -0.0007              | 5.0007                  |

### Conclusions
- The `map` function in `multiprocessing.Pool` performed better than the other multiprocessing methods but was still slower than sequential execution.
- The `apply` function was the slowest, indicating inefficient task distribution.
- `ProcessPoolExecutor` also exhibited poor performance compared to sequential processing.
- The negative values in Amdahl’s Law Speedup suggest that parallel execution introduced significant overhead, possibly due to synchronization and inter-process communication.

### Redoing the Test with 107 Numbers
(TODO: Add results after rerunning the test)

### Synchronous vs Asynchronous Pool
- **Synchronous Pool:** (TODO: Add observations and results)
- **Asynchronous Pool:** (TODO: Add observations and results)
- **Conclusion:** (Compare performance between synchronous and asynchronous methods)

## Part 2: Connection Management and Race Conditions

### Connection Access with More Processes Than Available Connections

- Observations:
  - Some processes were waiting for connections.
  - Multiple processes acquired the same connection in sequence.
  - Processes had to wait for a connection to be released before proceeding.

### Role of Semaphores

- **Prevention of Race Conditions:**
  - Semaphores limit the number of processes accessing a shared resource.
  - Prevents multiple processes from modifying a resource simultaneously.

- **Ensuring Safe Access:**
  - The semaphore ensures that only a limited number of processes can acquire a connection at a given time.
  - Once a process releases a connection, another waiting process can acquire it safely.

## Future Improvements
- Optimize task chunking to improve multiprocessing efficiency.
- Experiment with different pool sizes and connection limits.
- Profile inter-process communication overhead.

## How to Run the Code

```bash
python main.py
```


