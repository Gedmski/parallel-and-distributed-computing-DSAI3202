# Lab 3 Part 1: Data Parallel Model

## Author
**Gabriel Marquez**

---

## 📌 Objectives

- Build a data parallel model program using **threads** in Python.
- Build a data parallel model program using **processes** in Python.
- Understand the basics of **parallel programming** using Python’s `threading` and `multiprocessing` modules.

---

## 🧪 Experiment Summary

We computed the sum of numbers in the range **(0, 1,000,001)** using three approaches:

### 🔹 Sequential Execution
```
The sum for range (0, 1000001) is 500000500000
Total time taken: 0.048419 seconds
```

### 🔹 Threading (6 threads)
```
Total time taken: 0.054048 seconds
Speedup: 0.8959
Efficiency: 0.1493
Amdahl's Law: 1.7143
Gustafsson's Law: 10.2857
```

### 🔹 Multiprocessing (6 processes)
```
Total time taken: 0.018350 seconds
Speedup: 2.6387
Efficiency: 0.4398
Amdahl's Law: 1.7143
Gustafsson's Law: 10.2857
```


---

## ⚙️ Tasks Overview

### ✅ 3.a. Sequential Case
- A basic Python script calculated the sum from 1 to 1,000,000.
- Execution time was measured using the `time` module.

### ✅ 3.b. Parallelization with Threading
- The summation task was divided among 6 threads.
- Each thread was assigned a subrange to compute in parallel.
- Final result was collected and summed.
- Execution time slightly increased due to GIL limitations.

### ✅ 3.c. Parallelization with Multiprocessing
- The summation task was divided among 6 processes.
- Each process executed in its own memory space, avoiding GIL.
- Significantly better performance than both sequential and threaded versions.

---

## ❓ Questions & Answers

### 1. How does the execution time change from sequential to threaded to multiprocessing?

- **Sequential**: ~0.0484 seconds  
- **Threading**: ~0.0540 seconds — slightly slower due to Python's GIL.  
- **Multiprocessing**: ~0.0184 seconds — significantly faster due to parallel CPU usage.

### 2. Performance Metrics

| Metric                | Threading | Multiprocessing |
|----------------------|-----------|-----------------|
| **Speedup**          | 0.896     | 2.639           |
| **Efficiency**       | 14.93%    | 43.98%          |
| **Amdahl’s Law**     | 1.714     | 1.714           |
| **Gustafsson’s Law** | 10.286    | 10.286          |

### 3. Are there performance differences?

Yes:
- **Threading** suffers due to the **Global Interpreter Lock (GIL)** in Python.
- **Multiprocessing** bypasses the GIL by using separate memory spaces and OS-level processes, leading to better parallel performance.

### 4. Challenges & Solutions

| Challenge                             | Solution                                      |
|--------------------------------------|-----------------------------------------------|
| Thread synchronization               | Carefully used shared variables with locks    |
| Managing inter-process communication | Used `multiprocessing.Queue` to aggregate results |
| Uneven division of work              | Calculated dynamic subranges to split data equally |

### 5. When to use Threading vs. Multiprocessing?

| Use Case                  | Recommendation       |
|--------------------------|----------------------|
| I/O-bound tasks           | ✅ Threading         |
| CPU-bound tasks           | ✅ Multiprocessing   |
| Lightweight concurrency   | ✅ Threading         |
| High-performance parallelism | ✅ Multiprocessing |

---

## ✅ Conclusion

- Python threading is simple but limited by the GIL.
- Multiprocessing achieves real parallelism and better performance for CPU-bound tasks.
- Proper data partitioning, synchronization, and communication handling are essential for parallel programming.

---
