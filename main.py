class Pet: # Blueprint class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self): # Shows details of the pet
        print(f"I am {self.name} and I'm {self.age} years old ")
    
    def speak(self): # Shows when a pet doesn't define speak
        print("I don't know what to say")

class Cat(Pet): # Inherits from the Pet class
    def __init__(self, name, age, color):
        super().__init__(name, age) # using super() to reference Pet class (super class) and pass name & age
        self.color = color # adding color definition
    
    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet): # Inherits from Pet class
    def speak(self):
        print("Woof")

class Dolphin(Pet):
    def sonar(self):
        print ("Locating fish swimming around me!")

# Instance of Pet class
p = Pet("Max", 7)
p.show()

# Instance of Cat class
c = Cat("Tom", 10, "Blue")
c.show()

# Instance of Dog class
d = Dog("Max", 7)
d.speak()

# Instance of Dolphin class
t = Dolphin("Timmy", 10)
t.speak()
t.sonar()