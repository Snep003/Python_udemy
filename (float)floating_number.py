# /////////////////////////////////////////////////////////
# Конвертация int float str
average_price = 17.5
price = int(average_price)

print(price)
print(type((price)))

str_temperature = '17.5'
temperature = float(average_price)
print(temperature)
print(type(temperature))

int_mass = 10
mass = float(int_mass)
print(mass)
print(type(mass))


# Числа с плавающей точкой можно округлять, для этого используется метод round()
# round() всегда округляет до ближайшего 17.25 > 17 ; 0.75 > 1 ; 0.25 > 0
# при этом функция round всегда возвращает число типа int
round_name = 17.25
print(round(round_name))

round_rate = 0.75
print(round(round_rate))

round_time = 0.25
print(round(round_time))
