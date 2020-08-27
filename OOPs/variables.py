from OOPs_23_Aug import classes as c
class car:
    Car_supported = ["BMW", "Audi", "Mercedes", "Ferrari"]

    def __init__(self):
        self.model = "BMW"
        self.make = "2019"
        self.version = "Petrol"

    def car_model(self):
        print(f"Car Model : {self.model} | make: {self.make} | version : {self.version}")


if __name__ == "__main__":
    car1 = c.car()
    car1.car_model()

    car2 = c.car()
    print(id(car1.Car_supported))
    print(id(car2.Car_supported))

    car3 = c.car()
    print(car3.Car_supported)
    car3.Car_supported.append("Lamborghini")

    print(car3.Car_supported)
    print(car2.Car_supported)