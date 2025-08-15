class Car:
    # инициализатор
    def __init__(self, max_speed, color, model):
        self.max_speed = max_speed
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f"Car {self.model} is driving to {location}")

if __name__ == "__main__":
    car_honda = Car(160, "silver", "Honda Fit")
    car_subaru = Car(180, "black", "Subaru Forester")
    print(car_honda.max_speed, car_honda.color, car_honda.model)
    print(car_subaru.max_speed, car_subaru.color, car_subaru.model)
    car_subaru.drive_to_location("Tokmok")
    print(car_honda)