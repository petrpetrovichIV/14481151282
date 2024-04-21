class Huma():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


    def is_old(self):
        if self.age >= 40:
            return "is old"
        elif self.age >=18:
            return "is young"
        elif self.age >=13:
            return "is adult"
        elif self.age >=4:
            return "is child"
        elif self.age >=0:
            return "is baby"

    def __str__(self):
        return f"my name is {self.name} a im {self.age}my gender is {self.gender}"

human = Huma("David", 16, "male")

human.is