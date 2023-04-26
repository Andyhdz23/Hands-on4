import random

class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness_val = None

    def fitness(self):
        pass

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = '1' if self.genes[i] == '0' else '0'

    def crossover(self, other, crossover_rate):
        if random.random() < crossover_rate:
            crossover_point = random.randint(1, len(self.genes) - 1)
            new_genes = self.genes[:crossover_point] + other.genes[crossover_point:]
            return Chromosome(new_genes)
        else:
            return Chromosome(self.genes[:])

    @staticmethod
    def roulette_selection(population):
        fitness_sum = sum([chromosome.fitness_val for chromosome in population if isinstance(chromosome.fitness_val, int)])
        rand_val = random.uniform(0, fitness_sum)
        cum_sum = 0
        for chromosome in population:
            if isinstance(chromosome.fitness_val, int):
                cum_sum += chromosome.fitness_val
                if cum_sum > rand_val:
                    return chromosome
        return random.choice(population)

    @staticmethod
    def create_population(pop_size, chromosome_length):
        population = []
        for i in range(pop_size):
            genes = [random.choice(['0', '1']) for _ in range(chromosome_length)]
            chromosome = Chromosome(genes)
            population.append(chromosome)
        return population

    @staticmethod
    def is_finished(population):
        for chromosome in population:
            if chromosome.fitness_val == len(chromosome.genes):
                return True
        return False

    @staticmethod
    def genetic_algorithm(pop_size, chromosome_length, mutation_rate, crossover_rate, max_generations):
        population = Chromosome.create_population(pop_size, chromosome_length)
        generation = 1
        while generation <= max_generations and not Chromosome.is_finished(population):
            # Evaluate fitness of each chromosome
            for chromosome in population:
                chromosome.fitness_val = chromosome.fitness()
            # Create new population through selection, crossover, and mutation
            population = Chromosome.evolve_population(population, crossover_rate, mutation_rate)
            generation += 1
        # Return the first chromosome that has all genes set to 1, or the one with highest fitness value
        population.sort(key=lambda x: x.fitness_val or 0, reverse=True)
        return population[0]

    @staticmethod
    def evolve_population(population, crossover_rate, mutation_rate):
        new_population = []
        for i in range(len(population)):
            parent1 = Chromosome.roulette_selection(population)
            parent2 = Chromosome.roulette_selection(population)
            child = parent1.crossover(parent2, crossover_rate)
            child.mutate(mutation_rate)
            new_population.append(child)
        return new_population
