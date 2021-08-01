class Circle():

    def __init__(self, r) -> None:
        self.r = r

    def area(self):
        return self.r * self.r * 3.14

circle = Circle(2)
print(f'원의 면적: {circle.area()}')