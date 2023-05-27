from tires.tyres import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, Sensors) -> None:
        self.sensors = Sensors
        
    def needs_service(self):
        sum = 0
        for i in self.sensors:
            sum+=i
        if sum>=3:
            return True
        return False