def route_info(**dict):
    if dict.get('distance') and isinstance(dict['distance'], (int, float)):
        return f"Distance to you destination {dict['distance']}"
    if dict.get('speed') and dict.get('time'):
        return f"Distance to you destination {dict['speed'] * dict['time']}"

    return f"No distance info is available"


my_dict = {'distance': 1500}
my_dict_one = {'speed': 100, 'time': 5}
my_dict_tho = {'name': 'Alex'}

print(route_info(**my_dict))
print(route_info(**my_dict_one))
print(route_info(**my_dict_tho))
