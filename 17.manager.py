from optparse import Option


def add_item(myTemplist, item):
    myTemplist.append(item)
def find_index_item(myTemplist, item_name):
    result = -1
    lenght = len(myTemplist)
    for i in range(lenght):
        if myTemplist[i]['name']==item_name:
            result = i
    return result 
def remove_item(myTemplist, item_name):
    if find_index_item(myTemplist, item_name) >-1:
        del myTemplist[find_index_item(myTemplist.item_name)]
    else:
        print(item_name+"not in list")  
print("What do you want to do? -\n"\
        "1. Add\n" \
        "2. Remove")
option = int(input("select option 1 or 2: :"))
name_input = input("item name:")
expenses = list()
if option == 1:
    cost_input = int(input("Item cost: "))
    date_input = input("Date: ")
    item = {'name': name_input, 'cost':cost_input, 'date':date_input}
    add_item(expenses, item)
    print("Your expenses: ", expenses)
elif option == 2:
    remove_item(expenses, name_input)
    print("Your expenses: ", expenses)
else:
    print("Invalid input")  
