class Cat:
    def __init__(self):
        self.sound = "Meow Meow"

    def talk(self):
        return self.sound


class Dog:
    def __init__(self):
        self.sound = "Bow Bow"

    def talk(self):
        return self.sound


def main():
    c = Cat()
    d = Dog()

    print("Cat says: ", c.talk())
    print("Dog says: ", d.talk())
    print()
    print("Cat says: ", c.__class__.talk(Dog()))
    print("Dog says: ", d.__class__.talk(Cat()))


if __name__ == "__main__":
    main()
