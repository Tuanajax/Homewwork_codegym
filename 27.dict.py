def search(word,dict):
        return dict[word]
word = input("Enter number:")
dict_={"hi":"xin chao"}
if word in dict_: print(search(word,dict_))
else: print("Word not exist")     


        