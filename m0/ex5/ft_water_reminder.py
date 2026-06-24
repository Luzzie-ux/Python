# water reminder

"""
defines function that checks if plants needs water
"""


def ft_water_reminder() -> None:
    """
    function that reminds to water plants
    """
    dry = int(input("Days since last watering: "))
    if dry > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
    return
