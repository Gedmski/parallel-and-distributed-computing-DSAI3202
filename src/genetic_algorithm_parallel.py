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
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Track global best solution across all generations
    global_best_fitness = 1e6
    global_best_route = None

    start_time = time.time()

    # Load and validate the distance matrix
    distance_matrix = pd.read_csv('./data/city_distances.csv').to_numpy()
    assert not np.any(np.isnan(distance_matrix)), "Distance matrix contains NaNs!"
    assert np.all(distance_matrix.diagonal() == 0), "Diagonal should be zero (no self-distance)"

    # Parameters
    num_nodes = distance_matrix.shape[0]
    population_size = 10000
    local_population_size = population_size // size
    num_tournaments = 4
    mutation_rate = 0.1
    num_generations = 200
    stagnation_limit = 5

    np.random.seed(42 + rank)
    local_population = generate_unique_population(local_population_size, num_nodes)

    best_fitness = 1e6
    stagnation_counter = 0

    for generation in range(num_generations):
        # Evaluate local fitness
        local_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in local_population])

        # Gather all fitness values
        global_fitness_values = np.zeros(population_size, dtype=float)
        comm.Allgather(local_fitness_values, global_fitness_values)

        current_best_fitness = np.min(global_fitness_values)

        # Update global best if found
        if current_best_fitness < global_best_fitness:
            global_best_fitness = current_best_fitness
            best_idx = np.argmin(global_fitness_values)

            # Gather full population to retrieve the actual route
            all_populations = comm.allgather(local_population)
            global_population = [ind for sublist in all_populations for ind in sublist]
            global_best_route = global_population[best_idx]

            if rank == 0:
                print(f"[NEW GLOBAL BEST] Generation {generation}: {global_best_fitness}")

        # Check for stagnation
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            stagnation_counter = 0
        else:
            stagnation_counter += 1

        # Regenerate if stagnant
        if stagnation_counter >= stagnation_limit:
            if rank == 0:
                print(f"Regenerating population at generation {generation} due to stagnation")
            local_population = generate_unique_population(local_population_size, num_nodes)
            stagnation_counter = 0
            continue

        # Selection
        local_selected = select_in_tournament(local_population, local_fitness_values)

        # Crossover and Mutation
        offspring = []
        for i in range(0, len(local_selected), 2):
            parent1, parent2 = local_selected[i], local_selected[i + 1]
            child = order_crossover(parent1[1:], parent2[1:])
            offspring.append([0] + child)

        mutated_offspring = [mutate(route, mutation_rate) for route in offspring]

        # Replacement
        worst_indices = np.argsort(local_fitness_values)[-len(mutated_offspring):]
        for i, idx in enumerate(worst_indices):
            local_population[idx] = mutated_offspring[i]

        # Ensure uniqueness
        unique_population = set(tuple(ind) for ind in local_population)
        while len(unique_population) < local_population_size:
            individual = [0] + list(np.random.permutation(np.arange(1, num_nodes)))
            if calculate_fitness(individual, distance_matrix) < 1e6:
                unique_population.add(tuple(individual))
        local_population = [list(ind) for ind in unique_population]

        # Print best fitness of this generation (only on rank 0)
        if rank == 0:
            print(f"Generation {generation}: Best fitness = {current_best_fitness}")

    # Final output
    if rank == 0 and global_best_route is not None:
        print("Best Route:", [int(x) for x in global_best_route])
        print("Total Distance:", global_best_fitness)

    return time.time() - start_time