from engine.engine import Engine
from battery.battery import Battery
from servicable import Serviceable
from tires.tyres import Tyre

class Car(Serviceable):
    def __init__(self, eng, batt, tyre):
        self.engine =  eng
        self.battery = batt
        self.tires= tyre
                
    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service():
            return True
        return False
