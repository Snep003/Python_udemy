any_num = input("Input any number: ")

print(any_num)

# ответ будет 'str' так как любой вывод из input будет строкой
print(type(any_num))
# //////////////////////////////////////////////////////////////////////


user_input = input("Input any number: ")

any_num = int(user_input)

print(any_num)

# так как использована функция int() мы конвертируем целую строку в число int
print(type(any_num))
# можно конвертировать как строку, логическое значение, или с плавающей точкой, если передаем например слово, будет ошибка


# /////////////////////////////////////////////////////////////////////

# Конвертацию можно производить на одной строке кода

any_num = int(input("Enter any number: "))

print(type(any_num))

# ////////////
# Возведение в степень, для этого используется функция pow которой передается число и степень в которую необходимо возвести

base = 5
power = 3

print(pow(base, pow))  # 125

# Длинные числа
# В пайтон допускается разделение длинных числе при помощи нижнего подчеркивания
# для читабельности кода, при этом подчеркивание игнорируется
one_million = 1_000_000

print(one_million)  # 1000000

any_number = 3_427
print(any_number)  # 3427


# ////////////////////////////////ЗАДАНИЕ//////////////////////////

number_input = int(input("Enter any number: "))


print(number_input)

print(type(number_input))

number_one = 10.5
pow_number = 3

# pow отдает либо целое int или с плавающей точкой flow
print(pow(number_one, pow_number))
print(type(pow(number_one, pow_number)))
