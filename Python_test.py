import random

class GeneticAlgorithm:
    def __init__(self, target, population_size=100, mutation_rate=0.01):
        self.target = target
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self._initialize_population()

    def _initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = ''.join(random.choice('01') for _ in range(len(self.target)))
            population.append(individual)
        return population

    def _fitness(self, individual):
        return sum(1 for i, j in zip(individual, self.target) if i == j)

    def _crossover(self, parent1, parent2):
        crossover_point = random.randint(0, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def _mutate(self, individual):
        mutated_individual = ''
        for bit in individual:
            if random.random() < self.mutation_rate:
                mutated_individual += '0' if bit == '1' else '1'
            else:
                mutated_individual += bit
        return mutated_individual

    def evolve(self, generations=1000):
        for generation in range(generations):
            sorted_population = sorted(self.population, key=self._fitness, reverse=True)
            fittest_individual = sorted_population[0]
            if fittest_individual == self.target:
                print(f"Generation {generation}: {fittest_individual}")
                break

            new_population = [fittest_individual]

            while len(new_population) < self.population_size:
                parent1, parent2 = random.choices(sorted_population, k=2)
                child1, child2 = self._crossover(parent1, parent2)
                child1 = self._mutate(child1)
                child2 = self._mutate(child2)
                new_population.extend([child1, child2])

            self.population = new_population

            if generation % 100 == 0:
                print(f"Generation {generation}: {fittest_individual}")

if __name__ == "__main__":
    target_string = "Hello, World!"
    ga = GeneticAlgorithm(target_string)
    ga.evolve()
