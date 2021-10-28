# PyEvolution

The PyEvolution project offers a wide range of experimental evolutionary algorithms and genetic programming in python.

## Setup and Run

Run the main genetic algorithm using the following statement and arguments:

`"python main.py -i "<input_string: str>" -g <number of generations: int> -l <length of string: int>"`

* `"<input_string: str>"`: any kind of string that should be compared against
* `<number of generations: int>`: number of generations as int
* `<length of string: int>`: number of the string characters given as first argument as int

Example call: `"python main.py -i "party" -g 1000 -l 5"`

All subsequent iterations are carried out with a fixed set of parameters:

* `max_generations: int`: 100
* `improvement: float`: .0
* `time: int`: 10000

## Results

The output after optimization will look as follows:

```
<number of generation and related output>
***
Generation: 	100
Chromosomes: 	1000
Best Fitness: 	0.4
Best Solution: 	oaigy
***
Generation: 	101
Chromosomes: 	1000
Best Fitness: 	0.4
Best Solution: 	oaigy
***
-------------------------------
GENETIC ALGORITHM CONFIGURATION
-------------------------------
Selection Type: 	Rank Selection
Evaluation: 		By percentage of matching alleles
Crossover Type: 	Multipoint
Mutation Type: 		Swap
Survivor Select: 	Fitness Based
Time constraint: 	10000
Max Generations: 	100
Min Improvement: 	0.0
------------------------
STATISTICS
------------------------
Generations: 	102
Elapsed Time: 	1.4663465023040771
Best Fitness: 	0.4
Best Solution: 	oaigy
```

## Run Tests

Run tests using:

`python test\test_string_ga.py`