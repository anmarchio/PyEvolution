# this file tests the genetic algorithm with a predefined string
# a 4 letter word is given as input
# the test will then run on single functions and test them for input and output
input = "test"

def create_string_ga():
    pass
    # Example
# Random init ("test")
# Pop:
# 1: bjgd
# 2: hffh
# 3: trsc
# 4: jffj
# 5: zegj
#
# Eval
# Fitness: 0 / 0 / 0.5 / 0 / 0.25
#
# 50% Rank Select: trsc,zegj ?
#
# Mutate / Crossover
# Trsc, zegj
# 1: tegc
# 2: trgj
# 3: zesc
# 4: zrgc
# 5: trsc
# ***
# 6: zegj
# 7: zrsj
# 8: tegc
# 9: zrsc
# 10: tegj
# 11: trsj
# 12: zegc
#
# Survivor Selection (fitness):
# 0.5* / 0.25 / 0.25 / 0 / 0.5*
# 0.25 / 0.25*? / 0.25 / 0.25 / 0.5* / 0.5* / 0.25
#
# New pop:
# 1: tegc
# 2: trsc
# 3: zrsj
# 4: tegj
# 5: trsj
#
# Retry until termination criterion is met (100 genertions or 2 hours of elapsed time)
