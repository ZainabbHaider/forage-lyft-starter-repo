import unittest
from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapulet(unittest.TestCase):
    def test_should_be_serviced(self):
        current = 60000
        last_service_mileage = 20000 
        engine = CapuletEngine(current, last_service_mileage)
        self.assertTrue(engine.needs_service())
        
    def test_should_not_be_serviced(self):
        current = 60000
        last_service_mileage = 30000  
        engine = CapuletEngine(current, last_service_mileage)
        self.assertFalse(engine.needs_service())
   
class TestWilloughby(unittest.TestCase):
    def test_should_be_serviced(self):
        current = 80000
        last_service_mileage = 10000 
        engine = WilloughbyEngine(current, last_service_mileage)
        self.assertTrue(engine.needs_service())
        
    def test_should_not_be_serviced(self):
        current = 80000
        last_service_mileage = 50000 
        engine = WilloughbyEngine(current, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_should_be_serviced(self):
        warning_light = True
        engine = SternmanEngine(warning_light)
        self.assertTrue(engine.needs_service())
        
    def test_should_not_be_serviced(self):
        warning_light = False
        engine = SternmanEngine(warning_light)
        self.assertFalse(engine.needs_service())
    
if __name__ == '__main__':
    unittest.main()
    