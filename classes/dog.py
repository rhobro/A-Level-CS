class Dog:

    def __init__(self, name, breed, age, fluffiness):
        self.name = name
        self.breed = breed
        self.age = age
        self.fluffiness = fluffiness
        self.nose_moisture = 5

    def speak(self):
        print("woof")

    def canDrive(self):
        return self.age >= 4

    def getName(self):
        return self.name
    def setName(self, new):
        self.name = new

a = Dog("Ned", "Spaniel", 5, 3)
b = Dog("Ned", "Spaniel", 2, 3)
print(a.fluffiness)
a.speak()
a.name = "Ted"