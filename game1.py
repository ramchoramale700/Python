import random
def main():                                                            #function is used for this game
    options=["stone","paper","scissors"]                               #options for user 
    while True:                                                        #used for kepp game running until exist
        print("\nGAME ON")
        user=input("Enter your choice(stone/paper/scissors or exit):") #input from user
        if user == 'exit':                                             #if exit game will stop here
            print("Thanks For Playing !!")
            break
        if user not in options:                                        #if user enter invalid option 
            print("Invalied choice .Please try Again!")
            continue
        computer =random.choice(options)                               # hare computer will take random option
        print(f"Computer Choice :{computer}")
        if user == computer:
            print("It's adraw!")
        elif(user =="stone" and computer =="scissors") or \
            (user =="paper" and computer =="stone") or\
            (user =="scissors" and computer =="paper"):
            print("You win!")
        else:
            print("Computers Wins!")
main()   