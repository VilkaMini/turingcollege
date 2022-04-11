class Tesla:
    def __init__(self, model: str, color: str, autopilot: bool = False, efficiency: float = 0.3):
        self.__model = model
        self.__color = color
        self.__battery_charge = 99.9
        self.__autopilot = autopilot
        self.__is_locked = True
        self.__seats_count = 5
        self.__efficiency = efficiency
        
    def welcome(self) -> str:
        raise NotImplementedError

    @property
    def color(self) -> str:
      return self.__color

    def autopilot(self, obsticle: str) -> str:
      if self.__autopilot:
        return f"Tesla model {self.__model} avoids {obsticle}"
      else:
        return "Autopilot is not available"

    @property
    def seats_count(self) -> int:
      return self.__seats_count

    @seats_count.setter
    def seats_count(self, count: int) -> int:
      if (count >= 2):
        self.__seats_count = count
      else:
        print("Seat count cannot be lower than 2!")

    def unlock(self) -> bool:
      self.__is_locked = False

    @property
    def is_locked(self) -> bool:
        return self.__is_locked
    
    def open_doors(self):
      if self.__is_locked:
        return "Car is locked!"
      else:
        return "Doors opens sideways"

    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"
    
    def charge_battery(self):
        self.__battery_charge = 100
        self.check_battery_level()

    def drive(self, travel_range: float):
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
          self.__battery_charge -= battery_discharge_percent
          return self.check_battery_level()
        else:
          return self.check_battery_level()
