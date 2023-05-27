from battery.battery import Battery
from datetime import datetime

class SplendidBattery(Battery):
    def __init__(self,  Current_date, last_Service_date):
        self.last_service_date = last_Service_date
        self.current_date = Current_date
        
    def needs_service(self):
        print("in splendid")
        print(self.last_service_date)
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        print(service_threshold_date, self.current_date)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False