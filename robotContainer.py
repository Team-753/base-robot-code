from commands.exampleCommand import ExampleCommand
from subsystems.exampleSubsystem import ExampleSubsystem
from commands2 import button
import commands2

class RobotContainer:
    
    def __init__(self) -> None:
        # initiate your buttons first
        self.xboxController = button.CommandXboxController(0) # first USB slot
        # then initiate your subsystems
        self.exampleSubsystem = ExampleSubsystem("bruh", "moment")
        # then initiate your button bindings
    
    def configureButtonBindings(self) -> None:
        ''' Binds certain buttons to commands '''
        aButton = self.xboxController.A()
        aButton.whileTrue(ExampleCommand("hello", "world")) # runs whenever the button is pressed
        
    def getAutonomousCommand(self) -> commands2.Command:
        ''' Returns the designated autonomous command '''
        return None # does nothing