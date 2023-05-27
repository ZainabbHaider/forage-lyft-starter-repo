from engine.engine import Engine
from battery.battery import Battery
from servicable import Serviceable

class Car(Serviceable):
    def __init__(self, eng, batt):
        self.engine =  eng
        self.battery = batt
                
    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        return False
