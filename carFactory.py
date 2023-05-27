from car import Car
from battery.splendid_battery import SplendidBattery 
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery 
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage): 
        battery = SplendidBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage): 
        battery = SplendidBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    
    def create_palindrome(current_date, last_service_date, warning_light_on): 
        battery = NubbinBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light_on)
        return Car(engine, battery)
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage): 
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage): 
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    