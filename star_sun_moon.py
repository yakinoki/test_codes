import random

card_marks = 'star,sun,moon'
marks = card_marks.split(',')
print(marks)
print('moonは' + str(marks.index('moon')) + '番目')
print(marks[-2])

mark = random.choice(marks)
print(mark)

marks.sort()
print(marks)
marks.remove('star')
print(marks)