#garden data

class Plant():
    def __init__(self, name, height, age):
        self.name
        self.height
        self.age
    def show(name, height, age):
        print(f"{name}: {height}cm, {age} days old")

def main():
    print("=== Garden Plant Registry ===")
    Plant.show("Rose", 25, 30)
    Plant.show("Sunflowe", 80, 45)
    Plant.show("Cactus", 15, 120)

if __name__ == "__main__":
    main()
