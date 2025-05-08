
# Доступ к значению словаря через переменную
my_motorbike = {
    'brand': 'Ducati',
    'price': 12000
}
key_name = 'brand'
my_motorbike[key_name] = 'bmw'
print(my_motorbike)

# Вложенные словари
my_motorbike = {
    'brand': 'Ducati',
    'price': 12000,
    'price info': {
        'price': 25000,
        'is avalible': True
    }
}
# Доступ к значениям словаря
print(my_motorbike['price info']['price'])

# Использование переменных
brand = 'ADC'
bike_price = 12000
engine_vol = 1.2
my_motorbike = {
    'brand': brand,
    'price': bike_price,
    'engine_vol': engine_vol,
}
print(my_motorbike)
