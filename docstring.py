def mult_by_factor(value, mult=1):
    """Помножує число на мультиплікатор"""
    return value * mult


mult_by_factor(2)


def print_number_info(num):
    """
    Prints whether number is even or odd

    Args:
        num (int): Number to be a evaluated
    """
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")


print_number_info()


def print_number_info(num):
    """Prints num information

    Args:
        num (int): Integer number

    Returns:
        int: same number
    """
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")
    return num


def squere_num(num):
    print("Squere num is", num*num)


def process_number(num, calback_fn):
    calback_fn(num)


entered_num = int(input("Input any number:"))

process_number(entered_num, print_number_info)
process_number(entered_num, squere_num)
