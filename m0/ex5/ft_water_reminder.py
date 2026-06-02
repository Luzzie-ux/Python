def ft_water_reminder():
    dry = int(input("Days since last watering: "))
    if (dry > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
