from re import A
from tracemalloc import start


b = input("Enter: ")
list_=(b.split(",",3))
S1 = int(list_[0])
S2 = int(list_[1]) 

if S1 > S2:
    for i in range(S2,S1+1,1):
        a = " FizzBuzz" if i%3==0 and i%5==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i
        print(f"{a}",end=";")
else: print("re enter")
