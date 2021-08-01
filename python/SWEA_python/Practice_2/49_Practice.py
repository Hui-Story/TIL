class Shape():

    def __init__(self) -> None:
        pass

    def area(self):
        return 0

class Square(Shape):

    def __init__(self, length) -> None:
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

square = Square(3)
print(f'정사각형의 면적: {square.area()}')