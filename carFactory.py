from car import Car
from battery.nubbingBattery import nubbingBattery
from battery.spindlerBattery import spindlerBattery
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine



class carFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = spindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = spindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(current_date, last_service_date, warning_light_on_boot):

        engine = SternmanEngine(warning_light_on_boot)
        battery = spindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = nubbingBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = nubbingBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car


