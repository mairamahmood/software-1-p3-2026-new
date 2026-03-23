import random

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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Reg Num':<10} {'Max Speed':<10} {'Speed':<10} {'Distance':<15}")
        print("-" * 50)
        for car in self.cars:
            print(f"{car.registration_number:<10} {car.max_speed:<10} {car.current_speed:<10} {car.travelled_distance:<15.2f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print("Invalid floor!")
            return
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning Elevator {elevator_number + 1} to floor {destination_floor}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number!")

    def fire_alarm(self):
        print("\nFIRE ALARM! Moving all elevators to bottom floor...")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i + 1}:")
            elevator.go_to_floor(self.bottom_floor)


# ------------------ Main Program ------------------ #

# ---- Test Elevator ----
print("\n--- Elevator Test ---")
h = Elevator(0, 10)
h.go_to_floor(5)
h.go_to_floor(0)

# ---- Test Building ----
print("\n--- Building Test ---")
b = Building(0, 10, 3)
b.run_elevator(0, 5)
b.run_elevator(2, 7)
b.fire_alarm()

# ---- Test Car Race ----
print("\n--- Car Race Test ---")
cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
grand_derby = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not grand_derby.race_finished():
    grand_derby.hour_passes()
    hours += 1
    if hours % 10 == 0:
        grand_derby.print_status()

grand_derby.print_status()
print(f"\nRace finished in {hours} hours!")