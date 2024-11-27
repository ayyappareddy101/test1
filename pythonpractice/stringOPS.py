string1 = 'sdsda REW ABC ads EEFh eFG Ab Whgf sHGF fd e sds7da @REW 0Wh@gf sHG432F _dgf  '
string2 = 'ABC aB Efg cccc ads adfgs FDSsfd 1fsd %sfd #$%#$%# 54342'
list_split1 = string1.split(" ")
list_split2 = string2.split(" ")

list1 = [str1.capitalize() for str1 in list_split1 if str1.isalpha() and len(str1) >= 3]

list2 = [str1.capitalize() for str1 in list_split2 if str1.isalpha() and len(str1) >= 3]

list3 = list1+list2

count_dict = {i: list3.count(i) for i in sorted(list3)}

list3_uni = sorted([word  for word, count in count_dict.items() if count <= 1])

common_tuple = tuple(sorted([word  for word, count in count_dict.items() if count == 1]))

ends_with = tuple(sorted([word  for word, count in count_dict.items() if count == 1 and  word.endswith('s')]))


print(list1)
print(list2)
print(list3)
print(count_dict)
print(list3_uni)
print(common_tuple)
print(ends_with)
