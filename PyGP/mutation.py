import random

class Mutation():
    # Bit Flip = 0
    # Random Resetting = 1
    # Swap Mutation = 2
    # Scramble Mutation = 3
    # Inversion Mutation = 4
    probability = 0.1

    def __init__(self, prob):
        self.probability = prob

    # bitflip for binary representation
    def bitflip( self, array = [] ):
        chr_flips = array.count() * self.probability          # selects the percentage (=probability) of chromosomes
        al_flips = array.alleles.count() * self.probability           # selects the percentage (=probability) of alleles
        for i in chr_flips:                                         # then randomly selects a part of elements
            chr_index = random.randint(0, array.count())
            chr = array[chr_index]
            for j in al_flips :
                al_index = random.randint(0, chr.alleles.count())   # randomly selects one allel
                if chr.alleles[al_index] == 0:
                    chr.alleles[al_index] = 1
                else:
                    chr.alleles[al_index] = 0
        return array

    # integer flip for integer representation
    def random_resetting( self, array = [], fromint=0, toint=9 ):
        chr_flips = array.count() * self.probability              # selects the percentage (=probability) of chromosomes
        al_flips = array.alleles.count() * self.probability               # selects the percentage (=probability) of alleles
        for i in chr_flips:
            chr_index = random.randint(0, array.count())         # then randomly selects a part of elements
            chr = array[chr_index]
            for j in al_flips:
                al_index = random.randint(0, chr.alleles.count())       # then randomly selects a one allel
                chr.alleles[al_index] = random.randint(fromint, toint)  # and assigns a random integer
        return array


    # swap values from two positions at random
    def swap_mutation( self, array = [] ):
        chr_flips = int(len(array) * self.probability) # selects the percentage (=probability) of chromosomes
        if chr_flips < 1:
            chr_flips = 1
        al_swaps = int(len(array[0].genes) * self.probability) # selects the percentage (=probability) of alleles
        if al_swaps < 1:
            al_swaps = 1
        for i in range(0,chr_flips):
            chr_index = random.randint(0, len(array)-1)  # then randomly selects a part of elements
            for j in range(0,al_swaps):
                al_index1 = random.randint(0, len(array[chr_index].genes)-1)  # then randomly selects allel 1
                al_index2 = random.randint(0, len(array[chr_index].genes)-1)  # then randomly selects allel 2
                if al_index1 != al_index2:
                    if al_index1 > al_index2:
                        al_index1_tmp = al_index1
                        al_index1 = al_index2
                        al_index2 = al_index1_tmp
                    tmp_allel1 = array[chr_index].genes[al_index1]
                    array[chr_index].genes[al_index1] = array[chr_index].genes[al_index2]
                    array[chr_index].genes[al_index2] = tmp_allel1
        return array

    # scrambles or shuffles a subset of the chromosome
    def scramble_mutation( self, array = [] ):
        raise Exception("Not imlemented, yet!")
        #return pop

    # inverts the genes of subset of the chromosome like their order
    def inversion_mutation( self, array = [] ):
        raise Exception("Not imlemented, yet!")
        #return pop
