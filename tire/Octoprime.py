from tire.tire import Tires
class Octoprime(Tires):

    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):

        if sum(self.tire_wear_sensors) >= 3:

            return True

        else:

            return False
