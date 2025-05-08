my_comment = "This is a short comment"

print(my_comment)

print(my_comment.replace('short', 'long'))  # функция замены строк

# my_comment = my_comment.replace('short', 'one')
print(my_comment)


# функция len считает кол-во елементов строки вместе с пробелами
print(len(my_comment))

print(my_comment[0])  # Указание индекса после переменной выводит Букву
# которая находится в этом индексе, по сути первую букву

# Указание индекса со знаком - віводит символі с конца строки
print(my_comment[-1])
print(my_comment[-5])

print(my_comment[3:7])  # Вівод с 3 индекса включительно по 7 не включительно

print(my_comment[3:])  # Віведу с индекса 3 до конца строки
print(my_comment[: 10])  # Вывод от 0 до 10 индекса


# Ищет кол-во совпадений в строке будь то одного символа или групі результат 2
print(my_comment.count('is'))
# результат 1
print(my_comment.count('This'))

number = 10
