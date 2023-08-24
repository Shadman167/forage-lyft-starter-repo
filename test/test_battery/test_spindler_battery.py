import unittest
from datetime import date
from battery.spindlerBattery import spindlerBattery

class TestSpindlerBattery(unittest.TestCase):

    def test_needs_service_true(self):

        last_service_date = date.isoformat("2017-07-20")
        current_date = date.isoformat("2023-08-23")
        battery = spindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service(self))

    def test_needs_service_false(self):
        last_service_date = date.isoformat("2023-09-20")
        current_date = date.isoformat("2023-08-23")
        battery = spindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service(self))


