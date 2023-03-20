import wpilib
import commands2
from robotContainer import RobotContainer
'''
How to simulate code: py -3 robot.py sim
How to deploy code: py -3 robot.py deploy

'''



class MyRobot(commands2.TimedCommandRobot):
    
    def __init__(self, period = 0.07) -> None:
        super().__init__(period)
        
    def robotInit(self):
        self.robotContainer = RobotContainer()
        self.autoCommand = commands2.Command()
        
    def disabledInit(self) -> None:
        ''''''
        return super().disabledInit()
            
    def testInit(self) -> None:
        return super().testInit()
    
    def testPeriodic(self) -> None:
        return super().testPeriodic()
    
    def autonomousInit(self):
        self.autoCommand = self.robotContainer.getAutonomousCommand()
        if (self.autoCommand != None):
            self.autoCommand.schedule()
    
    def disabledExit(self) -> None:
        pass
        
    def autonomousPeriodic(self):
        pass
        
    def teleopInit(self):
        if (self.autoCommand != commands2.Command()):
            self.autoCommand.cancel()
        
    def teleopPeriodic(self):
        '''This function is called periodically during operator control.'''
        pass
    
    def disabledPeriodic(self):
        ''' Runs while the robot is idle '''
        pass
        
    def disabledInit(self) -> None:
        '''self.driveTrain.coast()'''
        pass
    
    def testInit(self) -> None:
        pass
    
    def testPeriodic(self) -> None:
        pass
    
if __name__ == "__main__":
    wpilib.run(MyRobot)