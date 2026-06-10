"""
defines functions that will simulate plant growth over time
"""


class Plant():
    """
    class Plant that defines name, height and age of each plant
    """
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate
        self.initial_height = height

    def grow(self):
        self.height = round(self.height + self.growth_rate, 2)

    def aging(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def simulate_week(self):
        print(f"--- {self.name} starting state ---")
        self.show()
        for day in range(1, 8):
            self.grow()
            self.aging()
            print(f"Day {day}: ", end="")
            self.show()
        total_growth = round(self.height - self.initial_height, 2)
        print(f"Total growth after 7 days: {total_growth}cm\n")


def main():
    """
    main function
    """
    print("=== Garden Plant Registry ===\n")

    rose = Plant("Rose", 25, 30, growth_rate=1.5)
    rose.simulate_week()

    sunflower = Plant("Sunflower", 80, 45, growth_rate=3.0)
    sunflower.simulate_week()

    violet = Plant("Violet", 15, 120, growth_rate=0.8)
    violet.simulate_week()


if __name__ == "__main__":
    main()
