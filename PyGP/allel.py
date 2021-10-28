import random
import string

class Allel():
    # This abstact class will contain the allel representation of input data
    # and form the basis of a population
    value = None

    def __init__(self, val):
        if val != None:
            self.value = val

    def init_chars(self, count=1):
        alphabet = list(string.ascii_lowercase)
        self.value = random.sample(alphabet, count)

    def init_integers(self, count):
        x = 0
        alphabet = [x+1 for i in range(count)]
