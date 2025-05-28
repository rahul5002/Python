class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")
class Flyer:
    def fly(self):
        print(f"{self.name} flies")  
print("1. Single Inheritance:")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")
dog = Dog("Rex")
dog.speak()  
dog.bark()   

print("\n2. Multiple Inheritance:")
class Duck(Animal, Flyer):
    def swim(self):
        print(f"{self.name} swims")
duck = Duck("Donald")
duck.speak()  
duck.fly()    
duck.swim()   

print("\n3. Multilevel Inheritance:")
class Mammal(Animal):
    def feed_milk(self):
        print(f"{self.name} feeds milk")
class Cat(Mammal):
    def meow(self):
        print(f"{self.name} meows")
cat = Cat("Whiskers")
cat.speak()      
cat.feed_milk()  
cat.meow()       

print("\n4. Hierarchical Inheritance:")
class Cow(Animal):
    def moo(self):
        print(f"{self.name} moos")
cow = Cow("Bessie")
dog.speak()  
cow.speak()  

print("\n5. Hybrid Inheritance:")
class Bird(Animal):
    def chirp(self):
        print(f"{self.name} chirps")
class Parrot(Bird, Flyer):
    def talk(self):
        print(f"{self.name} talks")

parrot = Parrot("Polly")
parrot.speak()  
parrot.chirp()  
parrot.fly()    
parrot.talk()   