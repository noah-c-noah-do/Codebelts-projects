# string1 = 'False'
# string2 = ''
# for x in string1:
#     for y in string2:
#         if x == y:
#             print('True')
# else:
#     print('False')
# #     for y in range(0, len(string2)):
# #         if string1[x] == y in range(0, len(string2)):
# #             print('True')
# #     else:
# #         print('False')
# # #     for y in string2:
# #         if x != y:
# #             print('False')
# #         else:
# #             print('True')
# # # Code goes here
string1 = 'yes'
string2 = 'no'


def similar_letters(string1, string2):
    for x in string1:
        for y in string2:
            if x == y:
                return print('True')
    else:
        return print('False')
    pass
