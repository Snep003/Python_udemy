class Vehicle:
    def __init__(self, brand, model, year, fuel_lvl):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_lvl = fuel_lvl
        self.engine_on = False

    def __str__(self):
        return f"Vehicle brand: {self.brand}, Model: {self.model}, Year of issue: {self.year}, Fuel(%): {self.fuel_lvl}"

    def engine_running(self):
        if self.fuel_lvl > 0:
            print("Engine started!")
            self.engine_on = True
        else:
            print("Cannot start! No fuel.")

    def stop_engine(self):
        self.engine_on = False
        print("Engine stopped.")

    def refuel(self, amount):
        if (self.fuel_lvl + amount) <= 100:
            self.fuel_lvl += amount
            print(f"Refueled! Current fuel level: {self.fuel_lvl}%")
        else:
            self.fuel_lvl = 100
            print(f"Poured! Tank is full!")


class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_lvl, doors_count):
        super().__init__(brand, model, year, fuel_lvl)
        self.doors_count = doors_count
        self.engine_on = False

    def open_trunk(self):
        if self.engine_on == False:
            self.open_trunk = True
            print("Trunk opened!")
        else:
            print('Its impossible to open the trunk, lock up the car!')


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, fuel_lvl, has_sidecar):
        super().__init__(brand, model, year, fuel_lvl)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        if self.engine_on == True:
            print("Performing wheelie! 🏍️")
        else:
            print("Start the engine first!")


class Truck(Vehicle):
    def __init__(self, brand, model, year, fuel_lvl, cargo_capacity):
        super().__init__(brand, model, year, fuel_lvl)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, weight):
        if weight > self.cargo_capacity:
            print("Cannot load! Exceeds capacity.")
        else:
            self.cargo = weight
            print(f"Loaded {weight}kg cargo")

    def unload_cargo(self):
        self.cargo = 0
        print("Cargo unloaded!")


my_vehicle = Vehicle('BMW', 'E39', '2000', 0)
my_car = Car('BMW', 'E39', '2000', 10, 4)
print(my_vehicle)
my_car.engine_running()
my_car.open_trunk()
# print(my_vehicle.engine_on)
# my_vehicle.stop_engine()
# print(my_vehicle.engine_on)
# my_vehicle.refuel(1)
# print(my_vehicle)
