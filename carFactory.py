import random

from car import Car
from battery.nubbingBattery import nubbingBattery
from battery.spindlerBattery import spindlerBattery
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine
from tire.Octoprime import Octoprime
from tire.Carrigan import Carrigan



class carFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = spindlerBattery(last_service_date, current_date)
        tire = Carrigan(tire_wear_sensors)
        car = Car(engine, battery, tire)
        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = spindlerBattery(last_service_date, current_date)
        tire = Octoprime(tire_wear_sensors)
        car = Car(engine, battery, tire)
        return car

    def create_palindrome(current_date, last_service_date, warning_light_on_boot, tire_wear_sensors):

        engine = SternmanEngine(warning_light_on_boot)
        battery = spindlerBattery(last_service_date, current_date)
        tire = Carrigan(tire_wear_sensors)
        car = Car(engine, battery, tire)
        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = nubbingBattery(last_service_date, current_date)
        tire = Octoprime(tire_wear_sensors)
        car = Car(engine, battery, tire)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = nubbingBattery(last_service_date, current_date)
        tire = Carrigan(tire_wear_sensors)
        car = Car(engine, battery, tire)
        return car


