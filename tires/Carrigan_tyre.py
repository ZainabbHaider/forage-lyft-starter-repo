from tires.tyres import Tyre

class CarriganTyre(Tyre):
    def __init__(self, Sensors) -> None:
        self.sensors = Sensors
        
    def needs_service(self):
        for i in self.sensors:
            if i>=0.9:
                return True
        return False