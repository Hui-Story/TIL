class Rectangle():

    def __init__(self, width, length) -> None:
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

rec = Rectangle(4, 5)
print(f'사각형의 면적: {rec.area()}')