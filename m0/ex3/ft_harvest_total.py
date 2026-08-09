# harvest total

"""
defines function that counts total harvest
"""


def ft_harvest_total() -> None:
    """
    function that counts how much was harvested in three days
    """
    w1 = int(input("Day 1 harvest: "))
    w2 = int(input("Day 2 harvest: "))
    w3 = int(input("Day 3 harvest: "))

    total = w1 + w2 + w3
    print(f"Total harvest: {total}")
