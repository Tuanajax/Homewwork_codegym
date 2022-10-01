from re import A


num_=input("Enter number: ")
a = "even" if int(num_)%2 ==0 else "odd"
print(f"{num_} is {a}")