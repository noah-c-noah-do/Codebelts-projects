string1 = 'abcd'
string2 = 'efgh'

# same_count = 0
# for i in set(string1):
#     for j in set(string2):
#         if i == j:
#             same_count += 1
# if same_count > 0:
#     print('True')
# else:
#     print('False')
# # Code goes here
# pass
same_count = 0
for i in set(string1):
    for j in set(string2):
        if i == j:
            same_count += 1
if same_count > 0:
    print('True')
else:
    print('False')
# if same_count > 0:
#     return('True')
# else:
#     return('False')
# # Code goes here
# pass
