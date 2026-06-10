# plant age

"""
defines function that checks plant age
"""


def ft_plant_age():
    """
    function that says if plant is ready to harvest
    """
    age = int(input("Enter plant age in days: "))
    if (age > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
