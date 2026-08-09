# plant age

"""
defines function that checks plant age
"""


def ft_plant_age() -> None:
    """
    function that says if plant is ready to harvest
    """
    ready_to_harvest: int = 60
    age = int(input("Enter plant age in days: "))
    if age > ready_to_harvest:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
