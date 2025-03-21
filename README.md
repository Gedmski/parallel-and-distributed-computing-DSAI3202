# Lab 6 Part 1: Parallel Square Computation with mpi4py

## Author
**Gabriel Marquez**

## Overview

This lab demonstrates a distributed parallel Python program using `mpi4py` to compute the square of integers from 1 up to **1e8**, or as far as possible within a 300-second time limit. The workload is distributed across multiple machines using MPI (Message Passing Interface).

---

## File

- `calculate_squares.py` — Python script that performs parallel square computation using MPI.

---

## Instructions

### 3.a. Square Program

- Implements a `square(n)` function to compute the square of integers from 1 to `n`.
- Uses MPI to divide the range among available processes for parallel execution.

---

### 3.b. Environment Setup

Ensure all target machines:
- Have `mpi4py` installed.
- Support passwordless SSH from the main machine.
- Are accessible via SSH.

---

### 3.c. Distribute the Program

- Place `calculate_squares.py` in the same directory path on all machines.
- Create a `machines.txt` file on the main machine listing the hostnames or IP addresses of all machines (one per line).

---

### 3.d. Run the Program

Use the `mpirun` command with the appropriate number of processes and the host file to execute the script across all machines.

---

### 3.e. Observe Results

The **root process (rank 0)**:
- Collects results from all other processes.
- Prints:
  - Total number of squares computed
  - Highest square value
  - Time taken for computation

---

### 3.f. Extended Computation

The script has been modified to attempt computing squares up to **1e8**.

---

## 3.g. Bonus Challenge

**Objective**: Maximize the number of square computations within a **300-second** time limit.

### Final Result

- **Highest square computed**: `355702502464`
- **Total squares computed**: `9,990,802`
- **Time limit of 300 seconds reached**
