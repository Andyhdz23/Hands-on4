import random
from chromosome import Chromosome

def generate_initial_population(target_string_length):
    return Chromosome.create_population(pop_size=100, chromosome_length=target_string_length)

def check_termination_condition(population):
    for chromosome in population:
        if chromosome.fitness_val == len(chromosome.genes):
            return True
    return False

def evolve_population(population, crossover_rate, mutation_rate):
    new_population = []
    for i in range(len(population)):
        parent1 = Chromosome.roulette_selection(population)
        parent2 = Chromosome.roulette_selection(population)
        child = parent1.crossover(parent2, crossover_rate)
        child.mutate(mutation_rate)
        new_population.append(child)
    return new_population

def run_genetic_algorithm(target_string_length, crossover_rate, mutation_rate, max_iterations, target_string):
    population = generate_initial_population(target_string_length)
    generation = 1
    while generation <= max_iterations and not check_termination_condition(population):
        # Evaluate fitness of each chromosome
        for chromosome in population:
            chromosome.fitness_val = chromosome.fitness()
        # Create new population through selection, crossover, and mutation
        population = evolve_population(population, crossover_rate, mutation_rate)
        generation += 1
    # Return the first chromosome that has all genes set to 1, or the one with highest fitness value
    population.sort(key=lambda x: x.fitness_val, reverse=True)
    best_chromosome = population[0]
    print(f"Best Chromosome: {best_chromosome.genes}\nFitness Value: {best_chromosome.fitness_val}")

if __name__ == '__main__':
    target_string_length = 50
    crossover_rate = 0.8
    mutation_rate = 0.01
    max_iterations = 1000
    target_string = "1" * target_string_length

    run_genetic_algorithm(target_string_length, crossover_rate, mutation_rate, max_iterations, target_string)
