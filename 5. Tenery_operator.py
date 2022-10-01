from re import A


num_=input("Enter number: ")
tex_=num_+' '+"is {} number"
a = "even" if int(num_)%2 ==0 else "odd"
print(tex_.format(a))