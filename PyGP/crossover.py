import random

from PyGP.chromosome import Chromosome


class Crossover:
    # OnePoint = 1
    # Uniform = 2
    # Arithmetic = 3
    # DavisOrder = 2

    def crossover_parents( self, array = [], crossoverType=1):
        if crossoverType == 0:
            raise Exception("Not imlemented, yet!")
        if crossoverType == 1:
            array = self.multipoint(array)
        if crossoverType == 2:
            raise Exception("Not imlemented, yet!")
        if crossoverType == 3:
            raise Exception("Not imlemented, yet!")
        if crossoverType == 4:
            raise Exception('Not imlemented, yet!')
        return array

    def multipoint( self, array = [] ):
        parent1 = Chromosome()
        parent2 = Chromosome()
        offspring = []
        i = 0
        while i < len(array):
            if len(array) == 2:
                # Select chromosome 1 and 2 as parent
                # in case only two elements are given
                parent1 = array[0]
                parent2 = array[1]
                # set i to 1 in order to escape loop
                i = 1
            else:
                # Select parent 1 by index i
                # Select parent 2 randomly:
                #   if random int equals i add 1, or subtract 1 if it's the last element
                parent1 = array[i]
                parent2_index = random.randint(0, len(array) - 1)
                if parent2_index == i & i < len(array)  - 1:
                    parent2_index = parent2_index + 1
                if parent2_index == i & i == len(array)  - 1:
                    parent2_index = parent2_index - 1
                parent2 = array[parent2_index]
            # Randomly select 2 crossover points
            # Make sure they are not the first (0) or last (array.count()-1) element
            point1 = random.randint(1, len(array[0].genes)  - 2)
            point2 = random.randint(1, len(array[0].genes)  - 2)
            # Swap the segments within crossover points
            parent1_tmp = parent1
            parent2_tmp = parent2
            if point1 != point2:
                if point1 > point2:
                    point1_tmp = point1
                    point1 = point2
                    point2 = point1_tmp
                for j in range(point1, point2):
                    parent1_tmp.genes[j] = parent2.genes[j]
                    parent2_tmp.genes[j] = parent1.genes[j]
            if point1 == point2:  # same as one point crossover
                for j in range(0, point1 - 1):
                    parent1_tmp.genes[j] = parent2.genes[j]
                for j in range(point1, len(array[0].genes)-1):
                    parent2_tmp.genes[j] = parent1.genes[j]
            # after swap copy variables back to their originals
            parent1 = parent1_tmp
            parent2 = parent2_tmp
            offspring.append(parent1)
            i = i + 1
        return offspring
