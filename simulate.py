from robot import ROBOT
from simulation import SIMULATION
from world import WORLD


simulation = SIMULATION()
simulation.Run()

world = WORLD()
robot = ROBOT()

simulation.Get_Fitness()
