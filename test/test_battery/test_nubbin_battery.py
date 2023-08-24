import unittest
from datetime import date
from battery.nubbingBattery import nubbingBattery


class TestNubbinBattery(unittest.TestCase):

    def test_needs_service_true(self):
        last_service_date = date.isoformat("2023-07-10")
        current_date = date.isoformat("2023-08-23")
        battery = nubbingBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service(self))

    def test_needs_service_false(self):
        last_service_date = date.isoformat("2023-09-10")
        current_date = date.isoformat("2023-08-23")
        battery = nubbingBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service(self))
