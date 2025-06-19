def merge_list_to_dict(list1, list2):
    list_to_dict = list(zip(list1, list2))
    print(list_to_dict)


name = ['Alex', 'Jon', 'Leya']
age = [10, 15, 20]
merge_list_to_dict(name, age)
