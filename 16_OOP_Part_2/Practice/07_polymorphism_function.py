class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")


def make_speak(animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_speak(dog)
make_speak(cat)