# # Методи наборів
# photo_sizes = {'1920x1080', '980x740'}
# photo_sizes.add('740x280')
# # Добавление происходит при помощи сравнения хешей, если хеши елемента не совпадают,
# # с тем что есть то елемент будет добавлен
# print(photo_sizes)


# photo_sizes_2 = {'1920x1080', '980x740', '120x120', '400x400'}
# print(photo_sizes.union(photo_sizes_2))  # обьеденит именно во второй набор


# common = photo_sizes.intersection(photo_sizes_2)  # пересечение
# print(common)

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))  # общие елементы
print(other_set.intersection(my_set))  # результат тот же
print(my_set.intersection('abc'))  # пустой набор
print(my_set.intersection('abcd'))  # 'd'
# Происходит єто потому что при передаче 'abcd' єто то же самое что мі передадим
# список 'a' 'b' 'c' 'd', потому что строка єто итерируемій обьект, и так как
# в 'd' встречается в обоих наборах, результат пересечения будет 'b'

# Обьеденим два набора
print(my_set.union(other_set))  # результатом будет обьекты которые есть
# или в одном наборе, или в другом


# проверка вхождения елементов множества
print(other_set.issubset(my_set))  # Результатом будет False
# потому что other_set не является подмножеством my_set, в наборе other_set
# есть 'a' которій не входит в набор my set если убрать 'a' то будет True,
# ведь в єтом случае other_set будет подмножеством my_set
