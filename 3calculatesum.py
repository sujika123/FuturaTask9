a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if(a==b==c):
    s = a+b+c
    sum = 3 * s
    print("sum=",sum)
else:
    sum = a+b+c
    print("sum=",sum)


# print("Method2")
#
# def sum_thrice(x, y, z):
#     sum = x + y + z
#
#     if x == y == z:
#         sum = sum * 3
#     return sum
#
#
# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))