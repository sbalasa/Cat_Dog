# Cat_Dog
## Make a Cat Bark in Python

The headline must've been confusing to you, well here we will walk you through it:
Let's create two objects in python, one a cat object which meows and a dog object which barks.

```
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

c = Cat()
d = Dog()
```

This is how they naturally sound:

```
print("Cat says: ", c.talk())
print("Dog says: ", d.talk())

Cat says:  Meow Meow
Dog says:  Bow Bow
```

This is how you can make a Cat bark and a Dog meow ;)

```
print("Cat says: ", c.__class__.talk(d))
print("Dog says: ", d.__class__.talk(c))

Cat says:  Bow Bow
Dog says:  Meow Meow
```
