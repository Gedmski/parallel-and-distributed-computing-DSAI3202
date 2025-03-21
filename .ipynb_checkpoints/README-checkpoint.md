# Lab 2: First Parallel Programs

## Author
**Gabriel Marquez**

---

## 📌 Objectives

- Build your **first parallel programs** in Python using both `threading` and `multiprocessing`.
- Learn how to **measure execution time** of functions.
- Analyze the **performance** using speedup, efficiency, Amdahl’s Law, and Gustafsson’s Law.

---

## 🧪 Tasks Overview

### 🔹 2.a. Sequential Case

- **Function 1**: Generate 1,000,000 random characters and join them into a string.
- **Function 2**: Generate 1,000,000 random integers (1–100) and sum them.
- Execution was timed sequentially.

**⏱️ Time Taken (Sequential)**: `0.543955 seconds`

---

### 🔹 2.b. Threading

- A thread was created for each function and run in parallel.
- Execution was timed from start to end.

**⏱️ Time Taken (Threading)**: `0.589326 seconds`

---

### 🔹 2.c. Multiprocessing

- A separate **process** was created for each function.
- Execution time was measured similarly.

**⏱️ Time Taken (Multiprocessing)**: `0.342167 seconds`

---

## 📊 Performance Analysis

| Metric                  | Threading     | Multiprocessing |
|------------------------|---------------|-----------------|
| **Speedup**            | 0.923         | 1.590           |
| **Efficiency**         | 11.54%        | 19.87%          |
| **Amdahl’s Law**       | 1.896         | 1.896           |
| **Gustafsson’s Law**   | 15.166        | 15.166          |

---

## ❓ Conclusions

- **Threading** does **not improve performance** in this case. In fact, it slightly increased execution time due to Python’s **Global Interpreter Lock (GIL)**, which prevents true parallel execution of CPU-bound tasks.
- **Multiprocessing** provided a **noticeable speedup** and better efficiency by leveraging multiple CPU cores. It effectively bypasses the GIL by running in separate memory spaces.
- For **CPU-bound** tasks like these, **multiprocessing is significantly more effective** than threading.
- Python's threading can still be useful for **I/O-bound** operations, but is limited in heavy computation scenarios.

---

## ✅ Summary

This lab demonstrated how basic operations can be parallelized and how **parallel design choices** (threads vs. processes) can **impact performance** in Python.

---
