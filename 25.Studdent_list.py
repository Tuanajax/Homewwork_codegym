
from ast import Delete
from typing_extensions import Self


class student_list():
    def __init__(self):
        self.tuple=('ID','Name','Bithday')
        self.list_={1:("Vu Anh Tuan","19-02-1994"),2:("Do thi thu","04-12-1996")}
        
    def view(self):
        for i,j in self.list_.items():
             a, b, c = self.tuple
             print(a,":",i)  
             print(b,":",j[0])
             print(c,":",j[1])
             print("**************")
   
    def test(self,ID):
        if ID in self.list_: 
            return True
        else: False
    
    def add(self):
        
        Id = int(input("Enter Student'ID:"))
        while self.test(Id):
            Id = int(input("Re- enter:"))
        Name = input("Enter Student'name:")
        Birth = input("Enter Student'Birth: ")
        self.list_[Id]=(Name,Birth)
    
    def test_2(self,id):
        if id not in self.list_: 
            return True
        else: False
    
    def update(self):
        ID = int(input("Enter Student'ID:"))
        print(self.list_[ID])
        Name = input("Enter Student'name:")
        Birth = input("Enter Student'Birth: ")
        self.list_[ID]=(Name,Birth)
   
    def delete(self):
        ID = int(input("Enter Student'ID:"))
        while self.test_2(ID):
            ID = int(input("ID isn't exist, re-enter ID!"))
        print("Name: ",self.list_[ID][0])
        print("Birth:",self.list_[ID][1])
        print("-----------------------")
        del self.list_[ID]       
                                      
                                                          
Tuan=student_list()
Tuan.delete()
Tuan.view()
# Tuan.test(1)


    





