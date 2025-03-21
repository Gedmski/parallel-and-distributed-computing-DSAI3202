# Fleet Route Optimization Using Genetic Algorithm
## Author
Gabriel Marquez

## Fleet Management Using Genetic Algorithms (Single Vehicle Version)

### Objective
This project aims to optimize the delivery route for a **single vehicle** serving a fleet management task. Using a **Genetic Algorithm (GA)**, the goal is to find the shortest possible route that starts and ends at the depot (node 0), while visiting **each delivery location (node)** **exactly once**.

#### Constraints:
- The vehicle must start and end at the depot (node 0).
- Each delivery location must be visited once.
- The total distance traveled must be minimized.

The **city layout** is modeled as a **graph** with nodes representing delivery points and edges representing distances. These distances are defined in the file `city_distances.csv`. A value of `100000` denotes an infeasible path between two nodes.

---

### Description of the Code

The project consists of the following main files:

- `genetic_algorithms_functions.py` — Implements core components of the GA.
- `genetic_algorithm_trial.py` — Runs the sequential version of the GA.
- `main.py` — Runs the **parallelized version** of the GA using MPI.
- `city_distances.csv` — A CSV file containing the distance matrix.

#### Distance Matrix
- Size: 32 x 32
- Values: Integer distances (max 100); `100000` represents disconnected nodes.

---

### Completing the Functions

#### `calculate_fitness(route, distance_matrix)`
This function computes the total distance of a proposed route. It:
- Sums all consecutive distances in the route.
- Adds the distance from the last node back to the depot.
- Returns the **negative** of total distance (for minimization).
- Returns a large penalty (e.g., 1e6) if any edge is invalid (distance = 100000).

#### `select_in_tournament(population, scores, number_tournaments=4, tournament_size=3)`
This function selects the best individuals from the population using tournament selection:
- Runs multiple tournaments.
- In each tournament, selects `tournament_size` random individuals.
- Chooses the individual with the highest fitness (lowest distance).
- Repeats for the desired number of tournaments.

Other GA operators implemented include:
- `order_crossover`: Preserves order while mixing parents.
- `mutate`: Randomly swaps genes to introduce diversity.
- `generate_unique_population`: Ensures initial population diversity.

---

### Explain and Run the Algorithm

`genetic_algorithm_trial.py` (and `main.py`) performs the following:
1. Loads the city distance matrix.
2. Initializes a population of possible routes.
3. Repeats for a number of generations:
    - Evaluates the fitness of each route.
    - Selects the best routes.
    - Applies crossover and mutation.
    - Tracks the best route found.
4. Prints the final route and total distance.

---

### Execution Times

- **Sequential Execution Time**: 7.77 seconds  
- **Parallel Execution Time (2 processes)**: 6.33 seconds  

---

### Parallelization

#### Parts Parallelized
- **Fitness Evaluation**: Each process evaluates the fitness of its local population.
- **Population Management**: Each MPI process manages a portion of the total population.
- **Best Fitness Tracking**: Values are shared and aggregated via MPI's `Allgather()`.

#### Implementation
- `main.py` uses `mpi4py` to parallelize population handling.
- Ensures unique populations per rank using different seeds.
- Aggregates global best route across all processes.

#### Performance Metrics

| Metric                      | Value      |
|----------------------------|------------|
| Speedup (S)                | 1.23×      |
| Efficiency (E)             | 61.37%     |
| Amdahl’s Law Speedup       | 1.82×      |
| Gustafson’s Law Speedup    | 1.90×      |

---

### Enhancements

#### Distributed over 2+ machines
- Code supports MPI distribution — tested with 2 processes.

#### Algorithm Improvements
- Implemented global best tracking.
- Stagnation detection and population regeneration.
- Early stopping based on fitness stagnation.

#### Performance Comparison
- Improved final fitness score and reduced execution time compared to baseline.
- Global best route preserved across generations.

---

### Final Result

#### Sequential Run
```
Best Solution: [0, 11, 7, 5, 4, 15, 26, 13, 27, 12, 31, 3, 18, 20, 24, 25, 10, 22, 28, 9, 21, 16, 8, 14, 2, 23, 17, 30, 19, 6, 29, 1]
Total Distance: 1224.0
```


#### Parallel Run (2 processes)
```
Best Route: [0, 2, 17, 25, 10, 7, 9, 11, 24, 20, 18, 5, 30, 27, 16, 22, 4, 28, 26, 29, 1, 21, 14, 6, 3, 15, 13, 19, 12, 31, 8, 23]
Total Distance: 1252.0
```

---

### Large-Scale Problem
#### Extended City Map
- Successfully ran the algorithm using city_distances_extended.csv (100 nodes).
- Algorithm completed in feasible time with valid output.

#### Scaling to Multiple Vehicles
To support multiple vehicles:
- Divide the node set into k clusters.
- Assign one vehicle per cluster.
- Each vehicle solves a TSP within its assigned nodes.
- Use additional optimization (e.g., k-means, capacity constraints) to balance workload.

---

### How to Run

```bash
# Sequential
cd src
python genetic_algorithm_trial.py

# Parallel (2 processes)
mpirun -n 2 python main.py
```