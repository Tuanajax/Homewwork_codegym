
from ast import Break
from pickle import TRUE
from random import randint
from re import A


while TRUE:
    current_number = 0
    a = randint(0,1)
    current_player = "human" if a==0 else "computer"
    while current_number <= 21:
        if current_player == "Human":
            player_choice = input("Player Enter:")
            while True:
                if int(player_choice) >=1 and int(player_choice) <=3: break
                else: 
                    player_choice =input("Player re-Enter:")
            print("Player'choice:",player_choice)
            current_number+= int(player_choice)
            if current_number  < 21: 
                current_player = "computer"
            else:
                print(current_number,"computer win")
                break     
        else:
            computer_choice = randint(1,3)
            print("computer' choice:",computer_choice)
            current_number += int(computer_choice)
            if current_number < 21:  current_player ="Human"
            else: 
                print(current_number,"Human win")
                break
            
    Ask_=input("Continue:(y/n):")
    if Ask_.upper()=="Y": continue
    else: break
                
        
        
    