# # # num = int(input())
# # # for i in range(1, num + 1):
# # #     j = int(input())
# # # if j % 7 == 0:
# # # #     print(int(j) ** 2)
# # # read = input()
# # # for i in read:
# # #     if read.isupper():
# # #         read = read + "_" + str.lower(i)
# # # print(read)

# # # # -3, 0, 3, 6, 12
# # # a = int(input())
# # # b = int(input())
# # # c = 0
# # # count = 0
# # # for i in range(a, b + 1):
# # #     if i % 3 == 0:
# # #         c = c + i
# # #         count += 1
# # # print(c/count)

# # # num = int(input())
# # # count = 0
# # # for i in range(1, num + 1):
# # #     i = int(input())
# # #     count += i
# # # print(count / num)

# # # digits = ['zero', 'one', 'two', 'three', 'four',
# # #           'five', 'six', 'seven', 'eight', 'nine']
# # # num = input()
# # # for char in num:
# # #     print(digits[int(char)])


# # # if a number is multiple of 3, print "Fizz" instead of this number
# # # if a number is multiple of 5, print "Buzz" instead of this number
# # # for numbers that are multiples of both 3 and 5, print "FizzBuzz"
# # # print the rest of the numbers unchanged.

# # for i in range(1, 101):
# #     if i % 3 == 0 and i % 5 == 0:
# #         i = 'FizzBuzz'
# #     elif i % 3 == 0:
# #         i = 'Fizz'
# #     elif i % 5 == 0:
# #         i = 'Buzz'
# #     print(i)


# x = 0
# count = 0
# a = input()
# while a != '.':
#     x += int(a)
#     count += 1
#     a = input()
# print(x / count)

stuff1 = []
stuff2 = []
cafe = input()
cafe_split = cafe.split()
print(cafe_split)
print(cafe_split[0])
print(cafe_split[1])
stuff1.append(cafe_split[0])
stuff2.append(cafe_split[1])
cafe2 = input()
cafe2_split = cafe2.split()
print(cafe2_split)
print(cafe2_split[0])
print(cafe2_split[1])
stuff1.append(cafe2_split[0])
stuff2.append(cafe2_split[1])
print(stuff1)
print(stuff2)

# cafe_names = []
# cafe_cats = []
# while input() != 'MEOW':
#     cafe = input()
#     cafe_split = cafe.split()
#     cafe_names += cafe_split[0]
#     cafe_cats += cafe_split[1]
# else:
#     print(cafe_names)
#     print(cafe_cats)
