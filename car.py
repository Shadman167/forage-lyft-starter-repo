import Serviceable
from battery.battery import Battery
from engine.engine import Engine
import Serviceable


class Car(Engine, Battery):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery


    def needs_service(self):
        pass
