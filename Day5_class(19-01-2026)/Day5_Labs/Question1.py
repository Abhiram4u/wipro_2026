class Vehicle:
    vehicle_count = 0
    def __init__(self):
        Vehicle.vehicle_count += 1
        print(f"vehicle count: {Vehicle.vehicle_count}")

    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("car object created")
    def drive(self):
        print("Car is being driven")

class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        print("Electric car object created")
    def charge(self):
        print("Electric car is charged")

if __name__ == "__main__":
    print("creating car: ")
    car = Car()
    car.start()
    car.drive()
    print("---------------- ")
    print("creating electric car: ")
    ecar = ElectricCar()
    ecar.start()
    ecar.drive()
    ecar.charge()

    print("\nTotal vehicles created: ", Vehicle.vehicle_count)