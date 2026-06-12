# garden data

"""
Garden data functions
"""


class Plant():
    """
    Class Plant that defines name, height and age of each plant
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        return


def main() -> None:
    """
    Main Function
    """
    print("=== Garden Plant Registry ===")
    Plant("Rose", 25, 30).show
    Plant("Sunflower", 80, 45).show
    Plant("Cactus", 15, 120).show
    return


if __name__ == "__main__":
    main()
