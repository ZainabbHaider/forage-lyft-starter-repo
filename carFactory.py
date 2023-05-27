from car import Car
from battery.splendid_battery import SplendidBattery 
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery 
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.Carrigan_tyre import CarriganTyre
from tires.Octoprime_tyre import OctoprimeTyre

class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, sensors=[0.1,0.2,0.3,0.4]): 
        battery = SplendidBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        tyre = CarriganTyre(sensors)
        return Car(engine, battery, tyre)
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, sensors=[0.1,0.2,0.3,0.4]): 
        battery = SplendidBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        tyre = OctoprimeTyre(sensors)
        return Car(engine, battery, tyre)  
      
    def create_palindrome(current_date, last_service_date, warning_light_on, sensors=[0.1,0.2,0.3,0.4]): 
        battery = NubbinBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light_on)
        tyre = CarriganTyre(sensors)
        return Car(engine, battery, tyre)
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, sensors=[0.1,0.2,0.3,0.4]): 
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        tyre = OctoprimeTyre(sensors)
        return Car(engine, battery, tyre)
        return Car(engine, battery)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, sensors=[0.1,0.2,0.3,0.4]): 
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        tyre = CarriganTyre(sensors)
        return Car(engine, battery, tyre)
    