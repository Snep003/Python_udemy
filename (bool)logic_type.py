is_authorized = True
print(is_authorized)
print(type(is_authorized))

print(100 > 24)
print(-5 > 0)
print("Long strint" > 'Long')
print([1, 2, 3] == [1, 2, 3])

db_is_available = False
print(db_is_available)
print(type(db_is_available))

print('//////////////////////////////////')

print(bool(10))
print(bool(-10))
print(bool([]))
print(bool([1, 2, 3]))
print(bool('list'))
print(bool(None))

print('//////////////////////////////////')

# Сравнивается побуквенно по юникоду, как только находится отличие
print("ver 1.25" > 'ver 1.1 ')
# проверка останавливается и принимается решение, все что дальше не проверяется, сильно влияет регистр

print(100 > 1)  # True
# True Сравнивается кол-во елем-тов в списке и значение
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] == [1, 2, 3, 4])  # False
# True Сравнивается название ключа и его значение
print({'key1': 1} == {'key1': 1})
print({'key1': 1} == {'key1': 2})  # False
print({'key1': 1, 'key2': 2} == {'key1': 1})  # False
