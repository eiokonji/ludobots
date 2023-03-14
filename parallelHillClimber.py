from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # delete files from old simulations
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del body*.urdf")
        os.system(f"del fitnessCurves\{c.populationSize}_{c.numberOfGenerations}_{c.seed}.txt")

        # relevant init section
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1 

    def Evolve(self):
        # evaluate each parent
        self.Evaluate(self.parents)
        # store best fitness for each generation - helper function
        self.Store_Best()
        self.Show_Best()
        # evolve several generations
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)
            self.Store_Best()

    def Evolve_For_One_Generation(self, currentGen):
        # spawn, mutate, evaluate, select for one gen
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print(currentGen)
        self.Select()

    def Evaluate(self, solutions):
        # solutions is a SOLUTION object
        # start the simulations in parallel for all parents
        for pop in range(c.populationSize):
            solutions[pop].Start_Simulation("DIRECT")
        # retrieve fitness values for each parent
        for pop in range(c.populationSize):
            solutions[pop].Wait_For_Simulation_To_End()

    def Spawn(self):
        # child is a copy of parent but with their own ID
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        # mutate each child
        for child in self.children:
            self.children[child].Mutate()

    # selection is no longer PHC; more tournament style
    def Select(self):
        # (1) all parents, children go into 1 big population
        self.everyone = []
        for key in self.parents:
            self.everyone.append(self.parents[key])
        for key in self.children:
            self.everyone.append(self.children[key])
        # (2) sort the whole population by creatures' fitness
        self.everyone.sort(key= lambda x: x.fitness, reverse= True)
        # (3) self.parent <- c.populationSize fittest creatures
        for i in range(c.populationSize):
            self.parents[i] = self.everyone[i]

    def Show_Best(self):
        # find and simulate parent with best fitness
        # returns the KEY
        best = max(self.parents, key= lambda x: self.parents[x].fitness)
        self.parents[best].Start_Simulation("GUI") 
        print(f"\nBest fitness: {self.parents[best].fitness: .3f}")

    def Store_Best(self):
        # works like Show_Best but stores it in a file instead
        # more for drawing the fitness plot
        # best <- KEY of most fit parent
        best = max(self.parents, key= lambda x: self.parents[x].fitness)
        bestFitness = self.parents[best].fitness
        
        f = open(f"FitnessData/{c.populationSize}_{c.numberOfGenerations}_{c.seed}.txt", "a")
        f.write(f"{bestFitness}\n")
        f.close()

    def Print(self, currentGen):
        # print parent and child fitness
        for key in self.parents:
            print(f"\nGen {currentGen} Fitness:")
            print(f"Parent: {self.parents[key].fitness: .3f} || Child: {self.children[key].fitness: .3f}")

