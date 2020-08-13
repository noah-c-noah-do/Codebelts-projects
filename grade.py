test1 = test2 = test3 = 90
final = 50
grade = 0.2 * (test1 + test2 + test3) + 0.4 * final
if 100 >= grade >= 90.0:
    letter = 'A'
elif 90 > grade >= 80.0:
    letter = 'B'
elif 80 > grade >= 70.0:
    letter = 'C'
elif 70 > grade >= 60.0:
    letter = 'D'
else:
    letter = 'F'
print(letter)
