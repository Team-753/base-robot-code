import commands2

class ExampleCommand(commands2.CommandBase):
    
    def __init__(self, parameterOne: str, parameterTwo: str) -> None:
        super().__init__()
        self.variableOne = parameterOne # these variables are now accessable
        self.variableTwo = parameterTwo # within any function in the class
        
    def initialize(self) -> None:
        ''' Ran when the command is first created '''
        return super().initialize()
    
    def execute(self) -> None:
        ''' Ran every robot loop until the command is finished '''
        print(f"{self.variableOne} {self.variableTwo}!")
    
    def end(self, interrupted: bool) -> None:
        ''' This code runs when the command ends '''
        return super().end(interrupted)
    
    def isFinished(self) -> bool:
        ''' This command is what determines if your command is over '''
        return super().isFinished()