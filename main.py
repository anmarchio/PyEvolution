import getopt

from PyGP.gp import GeneticAlgorithm

import sys


def main(argv):
    # Default arguments for
    # GeneticAlgorithm(max_generations: int, improvement: float, time: int)
    # runDefaultGP(InputString: string, number of generations: int, length of string: int)
    string = ""
    generations = 0
    length = 0
    try:
        opts, args = getopt.getopt(argv, "i:g:l:")
        for opt, arg in opts:
            if opt == '-i':
                string = arg
            if opt == '-g':
                generations = int(arg)
            if opt == '-l':
                length = int(arg)
    except getopt.GetoptError:
        print("Arguments not readable.")
        print("python main.py -i \"<input_string: str>\" -g <number of generations: int> -l <length of string: int>")
        sys.exit(2)
    ga = GeneticAlgorithm()
    ga.runDefaultGP(string, generations, length)


if __name__ == "__main__":
    main(sys.argv[1:])
