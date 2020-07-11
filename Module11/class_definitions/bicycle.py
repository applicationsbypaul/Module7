from Module11.class_definitions.rider import Rider


class Bicycle(Rider):

    def __init__(self):
        self.ride = 'Human powered, not enclosed, 2 wheels'
        self.rider = '1 or 2 if tandem'

    def rider(self):
        return self.ride

    def ride(self):
        return self.rider


class Motorcycle(Rider):

    def __init__(self):
        self.ride = 'Engine powered, not enclosed, 2 wheels'
        self.rider = '1 or 2'

    def rider(self):
        return self.ride

    def ride(self):
        return self.rider


class Car(Rider):

    def __init__(self):
        self.ride = 'Engine powered, enclosed, 4 wheels'
        self.rider = '1 up to 5 depending on the size'

    def rider(self):
        return self.ride

    def ride(self):
        return self.rider


# driver
bike = Bicycle()
motorcycle = Motorcycle()
car = Car()

print(bike.ride)
print(bike.rider)

print(motorcycle.ride)
print(motorcycle.rider)

print(car.ride)
print(car.rider)
