# count harvest iterative

"""
defined function that counts days until harvest
"""


def ft_count_harvest_iterative() -> None:
    """
    function that counts how many days till harvest
    """
    i = 1
    days = int(input("Days until harvest: "))
    while i < days + 1:
        print(f"Day {i}")
        if i == days:
            print("Harvest time!")
        i += 1
