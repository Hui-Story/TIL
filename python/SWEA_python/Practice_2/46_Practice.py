class Student():

    def __init__(self, name) -> None:
        self.name = name

class GraduateStudent(Student):

    def __init__(self, name, major) -> None:
        super().__init__(name)
        self.major = major

student1 = Student('홍길동')
print(f'이름: {student1.name}')

student2 = GraduateStudent('이순신', '컴퓨터')
print(f'이름: {student2.name}, 전공: {student2.major}')