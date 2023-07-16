# lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

lis = []
print("Enter the elements of list ")
for x in range(15):
    lis.append(int(input()))
print(lis)

uniqueList = []
duplicateList = []

for i in lis:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)

print("duplicateList is ",duplicateList)
print("uniqueList is ",uniqueList)


