# def goodbye(name):
#     print(f"Bye {name} !")


# def run_callback(name, callback):
#     callback(name)


# run_callback(name='Alex', callback=goodbye)

def short(name):
    print(name.upper())


def run_callback(name, callback):
    callback(name)


run_callback(name='alex', callback=short)
