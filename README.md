# Multiprocessing Performance Analysis

## Author
**Gabriel Marquez**

## Overview
This project evaluates the performance of different multiprocessing techniques in Python, analyzing their execution time, speedup, and efficiency. The tests compare sequential processing against:

- `multiprocessing.Pool(map)`
- `multiprocessing.Pool(apply)`
- `multiprocessing.Pool(apply_async)`
- `multiprocessing.Pool(map_async)`
- `concurrent.futures.ProcessPoolExecutor`

---

## Part 1: Performance Analysis

### Execution Times and Speedup

#### Test 1: 1,000,000 Numbers

| Method                           | Execution Time (s) | Speedup | Efficiency | Amdahl's Law Speedup | Gustafson's Law Speedup |
| -------------------------------- | ----------------- | ------- | ---------- | -------------------- | ----------------------- |
| **Sequential Processing**         | 0.0646            | 1.0000  | 1.0000     | N/A                  | N/A                      |
| **Multiprocessing Pool (map)**    | 0.2365            | 0.2731  | 0.0455     | -0.4008              | 5.2731                   |
| **Multiprocessing Pool (apply)**  | 165.7909          | 0.0004  | 0.0001     | -0.0004              | 5.0004                   |
| **Multiprocessing Pool (apply_async)** | 52.7717   | 0.0012  | 0.0002     | -0.0012              | 5.0012                   |
| **Multiprocessing Pool (map_async)**  | 0.2353     | 0.2745  | 0.0458     | -0.4039              | 5.2745                   |
| **ProcessPoolExecutor**           | 99.3798           | 0.0006  | 0.0001     | -0.0007              | 5.0006                   |

#### Test 2: 10,000,000 Numbers

| Method                           | Execution Time (s) | Speedup | Efficiency | Amdahl's Law Speedup | Gustafson's Law Speedup |
| -------------------------------- | ----------------- | ------- | ---------- | -------------------- | ----------------------- |
| **Sequential Processing**         | 0.6181            | 1.0000  | 1.0000     | N/A                  | N/A                      |
| **Multiprocessing Pool (map)**    | 1.8082            | 0.3418  | 0.0570     | -0.5685              | 5.3418                   |
| **Multiprocessing Pool (apply)**  | 1697.9181         | 0.0004  | 0.0001     | -0.0004              | 5.0004                   |
| **Multiprocessing Pool (apply_async)** | 498.4399  | 0.0012  | 0.0002     | -0.0012              | 5.0012                   |
| **Multiprocessing Pool (map_async)**  | 2.6384      | 0.2343  | 0.0390     | -0.3224              | 5.2343                   |
| **ProcessPoolExecutor**           | 1042.8648         | 0.0006  | 0.0001     | -0.0006              | 5.0006                   |

---

### Key Observations:

- **Multiprocessing using for loop** was not able to run due to too many processes happening at the same time.
- **Sequential Processing** was the fastest in both test cases.
- **Multiprocessing Pool (map)** and **map_async** performed better than other multiprocessing methods but were still slower than sequential processing.
- **Multiprocessing Pool (apply)** had the worst performance, indicating poor parallelization.
- **ProcessPoolExecutor** was also inefficient due to inter-process communication overhead.
- **Synchronous vs. Asynchronous Pools:**
  - The **asynchronous map_async** was slightly faster than its synchronous counterpart.
  - **apply_async** did not improve much over apply, likely due to process synchronization delays.

---

## Part 2: Connection Management and Race Conditions

### Connection Access with More Processes Than Available Connections

Observations:
- Multiple processes were waiting for connections.
- Processes sequentially acquired and released the same connection.
- The system suffered from contention, slowing down execution.

#### Example Output:
```
Process-0 is waiting for a connection...
Process-0 acquired Connection-2
Process-1 is waiting for a connection...
Process-1 acquired Connection-2 ...
Process-5 released Connection-2
```


### Role of Semaphores

#### **Preventing Race Conditions**
- Semaphores limit the number of processes that can access a resource at a given time.
- Prevents multiple processes from modifying a shared resource simultaneously.

#### **Ensuring Safe Access**
- A process must wait for an available connection before proceeding.
- Once a connection is released, another process can safely acquire it.

---

## Future Improvements

- **Optimize task chunking**: Reduce overhead and improve multiprocessing efficiency.
- **Experiment with different pool sizes**: Adjusting worker counts may impact execution speed.
- **Profile inter-process communication overhead**: Investigate bottlenecks affecting `ProcessPoolExecutor`.

---

## Summary:
This analysis highlights that while multiprocessing can theoretically speed up execution, the overhead of process management, inter-process communication, and contention can sometimes make sequential processing more efficient. Further optimizations are needed to take full advantage of parallelism.

---