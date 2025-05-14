list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

for i in list2:
    list1.append(i)
print(list1)


list4 = ["a", "b", "c"]
list5 = [1, 2, 3]
list4.extend(list5)
print(list4)