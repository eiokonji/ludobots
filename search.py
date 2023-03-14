from parallelHillClimber import PARALLEL_HILL_CLIMBER
import constants as c
import sys
import random

# take 3 inputs: no of generations, size of pop, seed
c.populationSize = int(sys.argv[1])
c.numberOfGenerations = int(sys.argv[2])
random.seed(int(sys.argv[3]))
c.seed = int(sys.argv[3])
if len(sys.argv) != 4:
    print("Not enough arguments")

# run evolution strategy
phc = PARALLEL_HILL_CLIMBER()
print(f"\nSeed: {c.seed}")
print(f"Number of Gens: {c.numberOfGenerations}")
print(f"Population per Gen: {c.populationSize}")
phc.Evolve()
phc.Show_Best()
