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
