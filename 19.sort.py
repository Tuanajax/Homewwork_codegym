from ast import Num


def sort(n_1,n_2,n_3):
    temp  =0
    if n_2 < n_3 and n_2<n_1:
        temp = n_1
        n_1 = n_2
        n_2 = temp
    elif n_3 < n_2 and n_3 < n_1:
        temp = n_1
        n_1 = n_3
        n_3= temp
    if n_3 < n_2:
        temp =n_2
        n_2 = n_3
        n_3 = temp
    return(n_1,n_2,n_3)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Original numbers: ", x, y, z)
print(sort(x,y,z))
