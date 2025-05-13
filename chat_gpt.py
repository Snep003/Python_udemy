# посчитать кол-во букв а е i o u
user_text = 'Hello, how a you doing?'.lower()

count_number_a = user_text.count('a')
count_number_e = user_text.count('e')
count_number_i = user_text.count('i')
count_number_o = user_text.count('o')
count_number_u = user_text.count('u')
print(count_number_a+count_number_e+count_number_i+count_number_o+count_number_u)

# Є рядок із цілим числом (наприклад, "3481").
# Витягни останню цифру та виведи її як int.


# Є рядок із цілим числом, наприклад "3481".
# Витягни останню цифру та виведи її як int.
str_number = '3481'
int_number = int(str_number[3])
print(int_number)
# Твоя програма повинна:
# Перетворити рядок на число з плаваючою крапкою (тип float).
# Піднести це число до квадрату.
# Вивести результат і тип змінної.

user_input = "1.75"
user_sq = float(user_input)**2
print(user_sq, type(user_sq))

# У тебе є два рядки: Твоя програма повинна:
# Перетворити обидва значення на числа (int).
# Знайти залишок від ділення a на b (оператор %).
# Вивести результат і тип.
a = "15"
b = "4"
a = int(a)
b = int(b)
print(a % b)


# Твоя програма повинна:
# Перетворити price_per_kg і weight_kg у числа з крапкою (float).
# Обчислити загальну ціну (price_per_kg * weight_kg).
# Вивести такий рядок (використовуючи f-string):
product = "Apples"
price_per_kg = "3.5"
weight_kg = "4"
price_per_kg = float(price_per_kg)
weight_kg = float(weight_kg)
total = price_per_kg * weight_kg
print(f"Total price for {weight_kg} kg, of Apples is {total} USD.")

# вивести з рядка окремо int та float, знайти сумму та перемножити
user_input = "12 3.5"
int_number = int(user_input[0:3])
float_number = float(user_input[3:6])
# print(int_number, type(int_number), float_number, type(float_number))
sum = int_number + float_number
mult = int_number * float_number
print(f'Sum is {sum}, product is {mult}')


# Користувач вводить рядок із двох чисел, розділених пробілом, наприклад "12.5 3".
# Розділіть рядок, перетворіть числа на float та виведіть їх суму, різницю, добуток і частку.
number = "12.5 3"
number = number.split()
number_one = float(number[0])
number_two = float(number[1])
print(number_one, type(number_one), number_two, type(number_two))
print(number_one + number_two, number_one - number_two,
      number_one * number_two, number_one/number_two)

# зробити з строки список чисел, вивести сумму всіх чисел
my_list = "4.5 3.1 6.8 2.2"
my_list = list(map(float, my_list.split()))

print(sum(my_list))

my_list = '12 3 7 9 4'
my_list = list(map(int, my_list.split()))
my_list.pop(1)
my_list.append(15)
my_list_copy = my_list.copy()
my_list_copy.pop()
all_list = my_list + my_list_copy
all_list.sort(reverse=True)
print(all_list)
print(len(all_list), all_list[0], all_list[-1])


# СЛОВНИКИ
info = {'product': 'laptop', 'price': 1200, 'available': True}
info['price'] = 1000
info['brand'] = 'Lenovo'

print(info)


student = {'name': 'Olena', 'group': 'KV-23', 'marks': [88, 92, 75]}
student['age'] = 19
student['marks'].append(85)
del student['group']
print(student)


student = {'name': 'Ivan', 'age': 20, 'course': 'Math'}
print(student.get('grade', 0))
del student['course']
print(student.keys())
print(student)
student_copy = student.copy()
student_copy['year'] = 2025
print(student, student_copy)
