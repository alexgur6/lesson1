class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def imya(self):
        print(f"Имя собаки: {self.name}")

    def vozrast(self):
        print(f"Возраст собаки: {self.age}")

    def sit(self):
        print(f'Собака сидит')

    def roll_over(self):
        print(f'Собака перекатывается')

my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()
my_dog.imya()
my_dog.vozrast()
print(f'')
my_dog = Dog('lucy', 3)
my_dog.sit()
my_dog.roll_over()
my_dog.imya()
my_dog.vozrast()