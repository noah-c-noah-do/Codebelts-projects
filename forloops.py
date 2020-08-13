# for item in range(10):
#     if item + 1 == 2:
#         print('two')
#     elif item + 1 == 3:
#         print('three')
#     else:
#         print(item + 1)
# string = 'codebelts'
# for letter in string:
#     print(letter)

# for x in range(10):
#     print(f"X:{x}")
#     for y in range(5):
#         print(f" Y:{y}")
#     print('END')

# x_count = 0
# y_count = 0

# for x in range(10):
#     x_count += 1
#     for y in range(5):
#         y_count += 1
#     print(x_count)
#     print(y_count)

for x in range(10):
    for y in range(5):
        if x == y:
            print(y)
        else:
            print(x)
