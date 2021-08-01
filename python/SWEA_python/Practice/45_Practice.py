import datetime

day = datetime.datetime.now()

name = str(input())
age = int(input())

year = day.year + (100 - age)

print(f'{name}(은)는 {year}년에 100세가 될 것입니다.')