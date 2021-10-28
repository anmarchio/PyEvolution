import time

# add abstract class to do the representation for external use of the code
# e. g. initialize population for signal processing and filter cascades
from PyGP import population


class GeneticAlgorithm:
    max_generations = 100
    min_improvement = .01
    max_time = 10000

    #def __init__(self):
    #    self.max_generations = 100
    #    self.min_improvement = 5

    def __init__(self, generations = 100, min_improv = .0, m_e_time = 10000):
        self.max_generations = generations
        self.min_improvement = min_improv
        self.max_time = m_e_time

    def runDefaultGP(self, target, pop_size, length):
        print("-----------------------------------")
        print("EVOLUTIONARY PROGRAMMING IN PYTHON")
        print("-----------------------------------")
        # Step One: Generate the initial population of individuals randomly. (First generation)
        pop = population.Population(None)
        pop.init_char_population(pop_size, length)
        # Step Two: Evaluate the fitness of each individual in that population (time limit, sufficient fitness
        # achieved, etc.)
        pop.evaluate_fitness(target, 0)
        #Step Three: Repeat the following regenerational steps until termination:
        term_criterion = 1
        iteration = 0
        elapsed_time = time.time()
        start_time = time.time()
        fitness_evolution = []
        while term_criterion == 1:
            # Evaluate the individual fitness of new individuals.
            pop.evaluate_fitness(target, 0)
            fitness_evolution.append(pop.fitness)
            # print generation / temporary result
            print("Generation: \t" + str(iteration))
            pop.print_state()
            # Select the best-fit individuals for reproduction. (Parents)
            # Breed new individuals through crossover and mutation operations to give birth to offspring.
            offspring = population.Population(None)
            offspring.elements = pop.select_crossover_mutate_and_survivor_selection()
            elapsed_time = time.time() - start_time
            term_criterion = self.check_criterion( pop, offspring, iteration, elapsed_time)
            iteration = iteration + 1
        # print results and statistics
        elapsed_time = time.time() - start_time
        self.print_stats( pop, iteration, elapsed_time)
        #self.print_chart(self, fitness_evolution)
        # save data
        # self.save_statistics_to_db(fitness_evolution)
        # self.save_statistics_to_file(fitness_evolution)
        return pop

    def print_stats(self, pop=population.Population, generations=0, elapsed_time=time):
        print("-------------------------------")
        print("GENETIC ALGORITHM CONFIGURATION")
        print("-------------------------------")
        print("Selection Type: \tRank Selection")
        print("Evaluation: \t\tBy percentage of matching alleles")
        print("Crossover Type: \tMultipoint")
        print("Mutation Type: \t\tSwap")
        print("Survivor Select: \tFitness Based")
        print("Time constraint: \t" + str(self.max_time))
        print("Max Generations: \t" + str(self.max_generations))
        print("Min Improvement: \t" + str(self.min_improvement))
        print("------------------------")
        print("STATISTICS")
        print("------------------------")
        print("Generations: \t" + str(generations))
        print("Elapsed Time: \t" + str(elapsed_time))
        print("Best Fitness: \t" + str(pop.fitness))
        print("Best Solution: \t" + pop.best_element_str())

    def print_chart(self, generations, pop=population.Population):
        for i in range(generations):
            print("-")

    def save_statistics_to_file( self ):
        raise Exception("Not imlemented, yet!")

    def save_statistics_to_db( self ):
        raise Exception("Not imlemented, yet!")

    def check_criterion(self, parents=population.Population(), offspring=population.Population(), iteration=0, elapsed_time=time):
        if(parents.fitness >= 1.0 )or offspring.fitness >= 1.0:
            return 0
        if(iteration > self.max_generations):
            return 0
        # check if there has been improvement in fitness > min_improvement
        if(abs(offspring.fitness - parents.fitness)*1.0 < self.min_improvement):
            return 0
        # check if there is too much elapsed time
        if(elapsed_time > self.max_time):
            return 0
        return 1
