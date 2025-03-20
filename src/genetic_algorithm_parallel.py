from mpi4py import MPI
import numpy as np
import pandas as pd
import time
from src.genetic_algorithms_functions import calculate_fitness, \
    select_in_tournament, order_crossover, mutate, \
    generate_unique_population

def genetic_algorithm_mpi():
    """
    Distributed Genetic Algorithm using MPI
    """
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()  # Process rank
    size = comm.Get_size()  # Total number of processes

    start_time = time.time()

    # Load the distance matrix
    distance_matrix = pd.read_csv('./data/city_distances.csv').to_numpy()

    # Parameters
    num_nodes = distance_matrix.shape[0]
    population_size = 10000
    num_tournaments = 4
    mutation_rate = 0.1
    num_generations = 200
    stagnation_limit = 5

    # Split population among processes
    local_population_size = population_size // size  # Divide population among processes
    np.random.seed(42 + rank)  # Ensure diversity across processes

    # Each process generates its portion of the population
    local_population = generate_unique_population(local_population_size, num_nodes)

    # Initialize variables for tracking stagnation
    best_fitness = int(1e6)
    stagnation_counter = 0

    for generation in range(num_generations):
        # **Step 1: Evaluate Fitness in Parallel**
        local_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in local_population])

        # Gather all fitness values from all processes
        global_fitness_values = np.zeros(population_size, dtype=float)
        comm.Allgather(local_fitness_values, global_fitness_values)

        # **Step 2: Find the Best Solution Across All Processes**
        current_best_fitness = np.min(global_fitness_values)

        # Track stagnation
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            stagnation_counter = 0
        else:
            stagnation_counter += 1

        # **Step 3: Handle Stagnation**
        if stagnation_counter >= stagnation_limit:
            if rank == 0:
                print(f"Regenerating population at generation {generation} due to stagnation")
            local_population = generate_unique_population(local_population_size, num_nodes)
            stagnation_counter = 0
            continue

        # **Step 4: Selection in Parallel**
        local_selected = select_in_tournament(local_population, local_fitness_values)

        # **Step 5: Crossover and Mutation**
        offspring = []
        for i in range(0, len(local_selected), 2):
            parent1, parent2 = local_selected[i], local_selected[i + 1]
            route1 = order_crossover(parent1[1:], parent2[1:])
            offspring.append([0] + route1)

        mutated_offspring = [mutate(route, mutation_rate) for route in offspring]

        # **Step 6: Replacement Strategy**
        worst_indices = np.argsort(local_fitness_values)[-len(mutated_offspring):]
        for i, idx in enumerate(worst_indices):
            local_population[idx] = mutated_offspring[i]

        # **Step 7: Ensure Population Uniqueness**
        unique_population = set(tuple(ind) for ind in local_population)
        while len(unique_population) < local_population_size:
            individual = [0] + list(np.random.permutation(np.arange(1, num_nodes)))
            unique_population.add(tuple(individual))
        local_population = [list(ind) for ind in unique_population]

        # Print best fitness (only rank 0 to avoid clutter)
        if rank == 0:
            print(f"Generation {generation}: Best fitness = {current_best_fitness}")

    # **Step 8: Determine the Best Solution**
    final_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in local_population])
    global_final_fitness_values = np.zeros(population_size, dtype=float)
    comm.Allgather(final_fitness_values, global_final_fitness_values)

    best_idx = np.argmin(global_final_fitness_values)
    best_solution = local_population[best_idx % local_population_size]  # Extract the correct process's solution

    if rank == 0:
        print("Best Solution:", [int(x) for x in best_solution])
        print("Total Distance:", calculate_fitness(best_solution, distance_matrix))

    return time.time() - start_time

# if __name__ == "__main__":
#     execution_time = genetic_algorithm_mpi()

#     # Print execution time for process 0
#     if MPI.COMM_WORLD.Get_rank() == 0:
#         print(f"Parallel Execution Time: {execution_time} seconds")
