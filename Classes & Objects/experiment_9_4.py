class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} makes a generic sound")
    
    def move(self):
        print(f"{self.name} moves")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks: Woof woof!")
    
    def move(self):
        print(f"{self.name} runs on four legs")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} chirps: Tweet tweet!")
    
    def move(self):
        print(f"{self.name} flies in the sky")

animal = Animal("Generic Animal")
dog = Dog("Buddy")
bird = Bird("Tweety")
print("--- Animal Actions ---")
animal.make_sound()
animal.move()

print("\n--- Dog Actions ---")
dog.make_sound()  
dog.move()        

print("\n--- Bird Actions ---")
bird.make_sound() 
bird.move()        