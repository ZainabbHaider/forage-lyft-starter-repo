import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery
from battery.splendid_battery import SplendidBattery

class TestSplendid(unittest.TestCase):
    def test_should_be_serviced(self):
        today = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2017-05-15")
        battery = SplendidBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
        
    def test_should_not_be_serviced(self):
        today = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-05-15")
        battery = SplendidBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
        
class TestNubbin(unittest.TestCase):
    def test_should_be_serviced(self):
        today = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2015-05-15")
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
        
    def test_should_not_be_serviced(self):
        today = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2017-05-15")
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
    
if __name__ == '__main__':
    unittest.main()
    