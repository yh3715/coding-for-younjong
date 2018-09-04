
class Person:

    def __init__(self, name, old, gender):
        self.name = name
        self.old = old
        self.gender = gender


class Colleague(Person):
    # position = "대리"
    def __init__(self, name, old, gender, position):
        super().__init__(name, old, gender)
        self.position = position

colleague = Colleague("윤종", "20", "남좌", "ceo")

print(colleague.__dict__)
