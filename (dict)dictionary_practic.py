my_disk = {}
# print(id(my_disk))
# print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

# print(my_disk)

print(my_disk.items())


my_dict = {}
my_dict[input('Введите название ключа 1 ')] = input('Введите ключ 1')
my_dict[input('Введите название ключа 2 ')] = input('Введите ключ 2')
my_dict[input('Введите название ключа 3 ')] = int(input('Введите ключ цифру'))
print(my_dict)
