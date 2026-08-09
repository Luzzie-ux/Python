# water reminder

"""
defines function that checks if plants needs water
"""


def ft_water_reminder() -> None:
    """
    function that reminds to water plants
    """
    max_days: int = 2
    dry = int(input("Days since last watering: "))
    if dry > max_days:
        print("Water the plants!")
    else:
        print("Plants are fine")
