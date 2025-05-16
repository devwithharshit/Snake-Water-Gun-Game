snake = r"""
                         .-=-.          .--.
             __        .'     '.       /  " )
     _     .'  '.     /   .-.   \     /  .-'\
    ( \   / .-.  \   /   /   \   \   /  /    ^
       \ `-` /   \  `-'   /     \   `-`  /
        `-.-`     '.____.'       `.____.'
"""
water = r"""
               _            
              | |           
__      ____ _| |_ ___ _ __ 
\ \ /\ / / _` | __/ _ \ '__|
 \ V  V / (_| | ||  __/ |   
  \_/\_/ \__,_|\__\___|_|   
                        
"""
gun = r"""
       _  __________=__
        \\@([____]_____()
       _/\|-[____]
      /     /(( )
     /____|'----'
     \____/          
"""
import random

while True:
    print("WELCOME TO SNAKE, WATER, GUN GAME!\nWhat do you want to Choose?:\nType, s for SNAKE, w for WATER, g for GUN")
    user_choice = input("Enter Your Choice: ")
    comp_choice = random.choice(["s", "w", "g"])
    print()
    reverse_dict = {"s" : "Snake", "w" : "Water", "g" : "Gun"}
    print(f"You Chose: {reverse_dict[user_choice]}")
    if user_choice == "s":
        print(snake)
    elif user_choice == "w":
        print(water)
    elif user_choice == "g":
        print(gun)
    else:
        print("Invalid choice")
    print(f"Computer Chose: {reverse_dict[comp_choice]}")
    if comp_choice == "s":
        print(snake)
    elif comp_choice == "w":
        print(water)
    elif comp_choice == "g":
        print(gun)
    else:
        print("Invalid choice")
    if comp_choice == user_choice:
        print("It's a DRAW!")
    else:
        if comp_choice == "s" and user_choice == "g":
            print("YOU WON!")
        elif comp_choice == "w" and user_choice == "s":
            print("YOU WON!")
        elif comp_choice == "g" and user_choice == "w":
            print("YOU WON!")
        elif comp_choice == "s" and user_choice == "w":
            print("YOU LOST!")
        elif comp_choice == "w" and user_choice == "g":
            print("YOU LOST!")
        elif comp_choice == "g" and user_choice == "s":
            print("YOU LOST!")
        else:
            print("SOMETHING WENT WRONG!")