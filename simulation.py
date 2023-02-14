import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
import time
from world import WORLD


class SIMULATION:
    def __init__(self, directOrGUI) -> None:
        self.directOrGUI = directOrGUI
        self.robot = ROBOT()
        self.world = WORLD()

        # set up environment
        if self.directOrGUI == "DIRECT":
            self.physicsCLient = p.connect(p.DIRECT)
        else:
            self.physicsCLient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # load world & robot
        p.setGravity(0, 0, -9.8)
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")
        self.robotId = p.loadURDF("body.urdf")

        # setup pyrosim
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Run(self):
        # keep the world open for c.iterations long
        for it in range(c.iterations):
            p.stepSimulation()

            # allow the robot to sense, pass down current timestep
            self.robot.Sense(it)

            # allow the robot to think, does nothing NOW
            self.robot.Think()

            # allow the robot to move, pass down current timestep
            self.robot.Act(it, self.robotId)

            if self.directOrGUI == "GUI":
                time.sleep(1/2400)
            
    def __del__(self):
        # destructor: disconnect from the simulator
        p.disconnect()
