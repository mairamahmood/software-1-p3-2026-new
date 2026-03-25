class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity  # in kWh


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume  # in liters



print("--- Publications Test ---")
magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
book1 = Book("Compartment No. 6", "Rosa Liksom", 192)

magazine1.print_information()
print()
book1.print_information()

print("\n--- Cars Test ---")


ecar = ElectricCar("ABC-15", 180, 52.5)
gcar = GasolineCar("ACD-123", 165, 32.3)

ecar.accelerate(120)
gcar.accelerate(110)

ecar.drive(3)
gcar.drive(3)

print(f"Electric car {ecar.registration_number} travelled {ecar.travelled_distance} km")
print(f"Gasoline car {gcar.registration_number} travelled {gcar.travelled_distance} km")