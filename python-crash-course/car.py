class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel=0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
    def fill_gas_tank(self,litres):
        self.fuel+=litres
    
class Battery:
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
        
class ElectricCar(Car):
    def __init__(self,make,model,year) -> None:
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery=Battery(75)
        
    def fill_gas_tank(self,litres=0):
        print("This car doesn't need a gas tank!")