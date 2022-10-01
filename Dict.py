
from typing_extensions import Self


class dict_2:
    def __init__(self):
        self.Volume = 0
        self.content ={"hi":["xinchao","ok"]}
        self.new_word = ""
    def intudien(self):
        for key, value in self.content.items():
            print("word:"+key)
            for el in value:
                print("Mean: ",el) 
            print()
    def checkexist(self,word):
        if word in self.content.keys():
            return True
        else:                        
            return False
    def creat_(self,input_word):
        d=input("Enter word's mean:")
        list_=list()
        list_.append(d)
        self.content[input_word] = list_
        
    def add(self):
        new = input(" Enter word:")
        while self.checkexist(new):
            new = input("re-enter word:")
        self.creat_(new)
        c = True
        while c:
            exit_= input("Nhap nghia moi khong: ")
            if exit_.upper()=="No": 
                c = False
            else: self.creat_(new)
mydict = dict_2()
mydict.add()
print(mydict.content)



