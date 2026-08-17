class Car:
    def __init__(self)->None:
        self.color = input("Enter the color of the car: ")
        self.type = input("Enter the type of the car: ")
        self.mileage = int(input("Enter the mileage of the car: "))
        self.seat_capacity = int(input("Enter the seat capacity of the car: "))

    def base_info(self):
        print(f"Car Info: Color: {self.color}, Type: {self.type}, Mileage: {self.mileage}, Seat Capacity: {self.seat_capacity}")


class Audi(Car):
    def __init__(self)->None:
        super().__init__()
        self.electric = bool(input("Is the car electric? (True/False): "))
        self.city = input("Enter the city of the car: ")

    def audi_info(self):
        self.base_info()
        print(f"Electric = {self.electric}")
        print(f"City = {self.city}")


c1=Audi()

c1.audi_info()
