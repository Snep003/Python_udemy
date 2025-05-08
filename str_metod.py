# Методи списків
# .append() позволяет добавить елемент в список, добавляется в конец списка
list_num = []
list_num.append(1)
list_num.append('apple')
list_num.append([1, 2, 3])
# print(list_num)

# метод pop - удаление елементов списка
inputs = [1, 2, 3]
inputs.pop()
# print(inputs)

# можно сохранять удаленный обьект списка таким образом
del_save = inputs.pop(0)
# print(inputs, del_save)

# можно сортировать список методом sort
post_ids = [245, 15, 22, 148]
post_ids.sort()  # Сортирует от меньшего к большему
print(post_ids)
post_ids.sort(reverse=True)  # Реверс сортировки от большего к меньшему
print(post_ids)
