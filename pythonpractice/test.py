list1 = [0,1,2,3,4,5,6]
list2 = [1,4,9,16,25,1,8,27,64,125,36]

# isSquares = False
#
# for i in list1:
#     if i**2 in list2:
#         isSquares = True
#     else:
#         isSquares = False
#         break
#
# print(isSquares)

# isSquare = all(i**2 in list2  for i in list1)

all(i**2 in list2  for i in list1)