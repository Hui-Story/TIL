class Person():

    def __init__(self) -> None:
        pass

    def getGender(self):
        return 'Unknown'

class Male(Person):

    def getGender(self):
        return 'Male'

class Female(Person):

    def getGender(self):
        return 'Female'

male = Male()
female = Female()
print(male.getGender())
print(female.getGender())