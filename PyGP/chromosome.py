import random

from PyGP.allel import Allel


class Chromosome:
    # Contains the default properties of a single chromosome
    genes = []
    score = .0

    def __init__(self, genes=None):
        self.genes = []

    def create_Random_Array(self, fromint, toint, length):
        # initialize random integers 0..10 in genes array
        genes = [random.randint(fromint, toint) for i in range(length)]

    def init_Char_Alleles(self, size):
        # creates an allel with a character
        # saves as many of them as defined by size in genes
        for i in range(size):
            new_allel = Allel(None)
            new_allel.init_chars(1)
            self.genes.append(new_allel)

    def string_match(self, string):
        # returns score indicating the percentage of matching characters
        # Addumption: genes is a string encoded variable
        self.score = 0.0
        if not string == None:
            char_allel = Allel(None)
            string = list(string)
            for i in range(0,len(string)):
                char_allel = self.genes[i]
                if string[i] == char_allel.value[0]:
                    self.score = self.score + 1.0
        self.score = self.score / len(string)
        return self.score
