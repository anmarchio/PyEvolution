from PyGP.chromosome import Chromosome
from PyGP.crossover import Crossover
from PyGP.evaluation import Evaluation
from PyGP.mutation import Mutation
from PyGP.selection import Selection


class Population():
    elements = None
    fitness = .0

    def __init__( self, *args ):
        if len(args) == 1:
            self.elements = args

    def init_random_int_population( self, fromint=0, toint=9, size=10 ):
        # In this example we create a population with the following properties:
        # size: 12 chromosomes
        # values: 0 ... toint 9 per gene
        self.elements = []
        for i in range(size):
            chr = Chromosome()
            chr.create_Random_Array(fromint, toint, size)
            self.elements.append(chr)

    def init_char_population( self, pop_size, length):
        self.elements = []
        for i in range(0,pop_size):
            chr = Chromosome()
            chr.init_Char_Alleles(length)
            self.elements.append(chr)
        print("Population size: " + str(len(self.elements)))

    def get_elements( self ):
        return self.elements

    # computes and return the best fitness in the population
    def evaluate_fitness( self, target, evaluationType ):
        eval = Evaluation()
        self.fitness = eval.evaluate_population(evaluationType, self.elements, target)
        return self.fitness

    def select_crossover_mutate_and_survivor_selection( self ):
        # Selection
        sel = Selection()
        parents = Population()
        parents.elements = sel.select_from_population(self.elements, 0, 0.1)
        # Crossover
        crsov = Crossover()
        parents.elements = crsov.crossover_parents(parents.elements, 1)
        # Mutation
        mut = Mutation(0.4)
        parents.elements = mut.swap_mutation(parents.elements)
        # Replace least-fit population with new individuals.    core = Core()
        survivors= sel.fitness_based_survivor_selection(parents.elements)
        return survivors

    def print_state( self ):
        print("Chromosomes: \t" + str(len(self.elements)))
        print("Best Fitness: \t" + str(self.fitness))
        print("Best Solution: \t" + self.best_element_str())
        print("***")

    def best_element( self ):
        index = 0
        best_fit = .0
        for i in range(len(self.elements)):
            if best_fit < self.elements[i].score:
                best_fit = self.elements[i].score
                index = i
        return self.elements[index]

    def best_element_str( self ):
        chr = self.best_element()
        solution = ""
        for i in range(len(chr.genes)):
            solution = solution + str(chr.genes[i].value[0])
        return solution

