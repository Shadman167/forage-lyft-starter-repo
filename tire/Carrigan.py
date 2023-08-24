from tire.tire import Tires


class Carrigan(Tires):

    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):

        for i in range(len(self.tire_wear_sensors)):

            if self.tire_wear_sensors[i] >= 0.9:
                return True

        return False
