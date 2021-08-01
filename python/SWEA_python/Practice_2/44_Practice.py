score = list(map(int, input().split(', ')))

class student():

    def __init__(self, score1, score2, score3) -> None:
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def sum_score(self):
        result = self.score1 + self.score2 + self.score3
        return result

student_score = student(score[0], score[1], score[2])
print(f'국어, 영어, 수학의 총점: {student_score.sum_score()}')