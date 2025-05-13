car = {'brand': 'bmw', 'model': '871', 'year': 2018}
car['color'] = 'black'
car_copy = car.copy()
car_copy.popitem()
print(car)
car_copy.clear()
print(car, car_copy)
