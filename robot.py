import constants as c
from motor import MOTOR
import os
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

# os.system delete call in this file! - brain, body

class ROBOT:
    def __init__(self, robotID):
        self.robotId = p.loadURDF(f"body{robotID}.urdf")
        self.nn = NEURAL_NETWORK(f"brain{robotID}.nndf")

        # setup pyrosim
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        # store each link and its sensor in self.sensors dict
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, it):
        # loop through dict and run GetValue method on each sensor
        for sensor in self.sensors.values():
            sensor.Get_Value(it) 

    def Think(self):
        self.nn.Update()

    def Prepare_To_Act(self):
        self.motors = {}
        # store each joint and its sensor in self.motors dict
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, it):
        # ...?
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle * c.motorJointRange)

    def Get_Fitness(self, id):
        fitness = self.__directionFitness(0) * -1
        f = open(f"tmp{id}.txt", "w")
        f.write(str(fitness))
        f.close()
        os.rename(f"tmp{id}.txt", f"fitness{id}.txt")

    def __directionFitness(self, param):
        # params: 0/x, 1/y, 2/z
        return p.getBasePositionAndOrientation(self.robotId)[0][param]