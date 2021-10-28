import math

from PyGP.chromosome import Chromosome


class Evaluation():
    #MCC = 1
    #FScore = 2
    #Exact = 3
    #YoudensJ = ?
    Score = 1

    def __init__(self):
        self.Score = 1

    def evaluate_population(self, evalType, elements, result):
        fitness = .0
        chr = Chromosome()
        if evalType == 0:
            i = 0
            while i < len(elements):
                chr = elements[i]
                chr.string_match(result)
                if fitness < chr.score:
                    fitness = chr.score
                i = i + 1
        TP = 0.0
        TN = 0.0
        FN = 0.0
        FP = 0.0
        if evalType == 1:
            while i < len(elements):
                chr = elements[i]
                #[TP, TN, FN, FP] = chr.get_accuracy()
                chr.score = self.MCC(TP, TN, FN, FP)
        if evalType == 2:
            beta = 2
            while i < len(elements):
                chr = elements[i]
                # [TP, TN, FN, FP] = chr.get_accuracy()
                chr.score = self.FScore(TP, TN, FN, FP, beta)
        return fitness
        # add further evaluation functions here

    def MCC(self, TP, TN, FN, FP):
        return (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))

    def FScore(self, TP, TN, FN, FP, beta):
        precision = TP / (TP + FP)
        recall = TP / TP + FN
        return 1 + math.pow(beta,2) * ((precision * recall) & ((math.pow(beta,2) * precision) + recall))
