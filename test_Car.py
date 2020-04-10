from Car import Car


def test_brake():
    car = Car(50)
    car.brake()
    assert car.speed == 45
