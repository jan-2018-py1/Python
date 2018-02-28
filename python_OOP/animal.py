
class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = 50
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def display_health(self):
        print "Health: " + str(self.health)
        return self

animal1 = Animal("Jonathan", 30)
animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def pet(self):
        self.health = self.health + 5
        return self

dog1 = Dog("Vania", 150)
dog1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def fly(self):
        self.health = self.health - 10
        return self
    def display_health(self):
        print "I am a Dragon"
        return self

dragon1 = Dragon("Yolanda", 500)
dragon1.walk().run().fly().fly().fly().display_health()

#animal2 = Animal("Basilio", 200)
#animal2.pet()
#animal2.fly()
#animal2.display_health()    
