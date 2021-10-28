class Selection():
    #Rank Selection = 0
    #RouletteWheel = 1
    #SUS = 2
    #Tournament = 3
    #Random = 4
    #Elitist = 5

    def select_from_population( self, pop_elements, selType=0, share=0.2 ):
        parent_elements = []
        index = 0
        if selType == 0: # rank selection
            #  sort by chromosome fitness
            sorted(pop_elements, key=lambda chromosome: chromosome.score)
            # only select the best ranked individual and create a new population
            elements_count = int(len(pop_elements) * share)
            if elements_count < 1:
                elemets_count = 1
            # return a share of the current population as parent
            for i in range(0, elements_count):
                parent_elements.append(pop_elements[i])
        if selType == 1:
            raise Exception("Not imlemented, yet!")
        if selType == 2:
            raise Exception("Not imlemented, yet!")
        if selType == 3:
            raise Exception("Not imlemented, yet!")
        if selType == 4:
            raise Exception("Not imlemented, yet!")
        if selType == 5:
            raise Exception("Not imlemented, yet!")
        return parent_elements

    def age_based_survivor_selection(self, parents):
        raise Exception("Not imlemented, yet!")

    def fitness_based_survivor_selection( self, offspring = []):
        survivors = []
        # sort population first, then select the best
        sorted(offspring, key=lambda chromosome: chromosome.score)
        for i in range(0, len(offspring)):
            survivors.append(offspring[i])
        return survivors
