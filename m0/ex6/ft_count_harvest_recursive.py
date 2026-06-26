# count harverst recursive

"""
this file defines the recursion helper and the count harvest with recursion
"""


def recursion_helper(days: int, i: int) -> None:
    """
    helper to allow the counting with recursion
    """
    if i != days + 1:
        print(f"Day {i}")
        i += 1
        recursion_helper(days, i)
    else:
        print("Harvest time!")
    return


def ft_count_harvest_recursive() -> None:
    """
    function that will call recursion helper to count
    """
    i: int = 1
    days: int = int(input("Days until harvest: "))
    recursion_helper(days, i)
    return
