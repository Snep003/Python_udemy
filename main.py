def merge_list_to_dict(list_1, list_2):
    return dict(zip(list_1, list_2))


list_1 = ['one', 'two', 'three']
list_2 = [1, 2, 3]

result = merge_list_to_dict(list_1, list_2)
print(result)
