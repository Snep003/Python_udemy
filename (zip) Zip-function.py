fruits = ['apple', 'banana', 'lime']
number = [100, 30, 15, 20]

fruit_zip = zip(fruits, number)
# print(fruit_zip)
# print(type(fruit_zip))

fruit_zip = list(fruit_zip)
# print(fruit_zip)


# Конвертация zip в dict
fruits = ['apple', 'banana', 'lime']
number = (100, 30, 15)
number_two = '123'
nabor_set = {10, 15, 70}
dictenary = list(zip(fruits, number, number_two, nabor_set))
print(dict)

# Задание у урока создать два списка товарі и цені товаров
# Обьеденить их функцией zip
# сконвертировать в список а потом в словарь
list_of_goods = ['cake', 'oil', 'bread', 'butter', 'set of vagitables']
price = [3, 2, 1, 2, 4]
specification = zip(list_of_goods, price)
specification_list = list(specification)
print(specification_list)
specification_dict = dict(specification_list)
print(specification_dict)
