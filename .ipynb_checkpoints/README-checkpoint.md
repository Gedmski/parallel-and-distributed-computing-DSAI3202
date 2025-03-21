# Lab 6 Part 2: MPI-Based Virus Spread Simulation

## Author
**Gabriel Marquez**

## Overview

This lab simulates the spread of a virus within a population using a parallel MPI-based program. Each process represents a segment of the population with a unique vaccination rate. The simulation models how infection spreads over time, taking into account vaccination effectiveness and chance of spread.

The program uses `mpi4py` to parallelize the simulation across multiple processes. Infection rates and vaccination rates are calculated per process to observe the dynamics of virus transmission.

---

## Key Features

- Parallel virus spread simulation using MPI
- Unique vaccination rates for each process
- Infection spread over time steps
- Final infection rate printed per process

---

## Output Sample

```
Process 0: Vaccination Rate = 0.46, Infection Rate = 0.31
Process 1: Vaccination Rate = 0.36, Infection Rate = 0.31
Process 2: Vaccination Rate = 0.41, Infection Rate = 0.31
...
Process 17: Vaccination Rate = 0.33, Infection Rate = 0.31
```

---

## Steps Implemented

### 4.a. Initialize MPI Environment

- Imported `mpi4py` and initialized the communicator.
- Retrieved the rank and total number of processes.

### 4.b. Define Parameters

- Set:
  - `population_size = 100`
  - `spread_chance = 0.3`
  - `vaccination_rate = np.random.uniform(0.1, 0.5)` (unique per process)

### 4.c. Initialize the Population

- Population represented as a NumPy array of 0s (uninfected).
- Rank 0 randomly infected 10% of its population.

### 4.d. Implement Virus Spread Function

- Function `spread_virus(population)` updates infection status based on spread chance and vaccination rate.

### 4.e. Simulate Virus Spread

- Ran the spread function over 10 time steps.
- Used MPI to share updated population arrays with the root process (rank 0), which aggregated data.

### 4.f. Calculate Infection Rate

- Infection rate per process = infected individuals / population size.
- Each process printed its own vaccination and infection rates.

### 4.g. Run and Experiment

- Ran with 18 processes.
- Observed consistent infection rates across processes, affected by randomized vaccination rates.
- Experimented with changing vaccination rates and spread chance to analyze impact.

---

## How to Run

1. Ensure `mpi4py` and `numpy` are installed.
2. Use `mpirun` or `mpiexec` to run the program across multiple processes.

Example:
```shell
mpirun -n 18 python main.py
```

## Observations
- Vaccination rate directly affects virus transmission.
- Infection rates remained similar across processes due to communication and data aggregation by the root process.
- Increasing vaccination rate can reduce or stabilize infection spread over time.

## Next Steps
- Extend to larger populations.
- Simulate localized interactions and more realistic social structures.
- Add recovery or mortality parameters for more complex modeling.