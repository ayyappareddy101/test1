def list_oper(list1,list2):
    # isSquares = all(i**2 in list2  for i in list1)
    # isCubes = all(i**3 in list2  for i in list1)
    # if isSquares and isCubes:
    #     return "Squares and cubes present"
    #
    # elif isCubes:
    #     return "Cubes present"
    #
    # elif isSquares:
    #     return 'Squares present'
    #
    # else:
    #     return 'So such pattern is present'
    return ("Squares and cubes present" if all(i**2 in list2 for i in list1) and all(i**3 in list2 for i in list1)
    else "Cubes present" if all(i**3 in list2 for i in list1)
    else "Squares present" if all(i**2 in list2 for i in list1)
    else "No such pattern is present")


list1 = [1,2,3,4,5,6]
# list2 = [1,4,9,16,25]
list2 = [1,4,9,16,25,1,8,27,64,125]
print(list_oper(list1,list2))
