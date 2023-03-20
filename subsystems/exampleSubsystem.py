import commands2

class ExampleSubsystem(commands2.SubsystemBase):
    
    def __init__(self, parameterOne, parameterTwo) -> None:
        super().__init__()
        self.variableOne = parameterOne # these variables are now accessable
        self.variableTwo = parameterTwo # within any function in the class
        
    def periodic(self) -> None:
        ''' This function is ran every robot loop '''
        return super().periodic()