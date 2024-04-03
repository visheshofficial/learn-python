from car import Car
class E_Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self,battery_size) -> None:
        self.battery_size=battery_size
    
    def describe_battery(self):
        print(f"This battery is of {self.battery_size}-kWh.")
    def get_range(self):
        if self.battery_size==75:
            range=260
        elif self.battery_size==100:
            range=315
        print(f"This car can go about {range} miles on a full charge.")
        
class E_ElectricCar(Car):
    def __init__(self,make,model,year) -> None:
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery=E_Battery(75)
        
    def fill_gas_tank(self,litres=0):
        print("This car doesn't need a gas tank!")