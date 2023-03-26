#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random

def rock_paper_scissor():
    # rock/paper/scissor by computer
    def pc_output(choice,inputu):
        if choice == 1:
            outputs = ['rock','paper','scissor'] #0.33

        elif choice == 2:
            outputs = ['rock','rock','paper','paper','scissor','scissor'] #0.2
            outputs.remove(inputu)

        else:
            outputs = ['rock','rock','rock','paper','paper','paper','scissor','scissor','scissor'] #0.142
            outputs.remove(inputu)
            outputs.remove(inputu)

        output = random.choice(outputs)
        print(f"PC has chosen: '{output}'")
        print()
        return output

    # difficulty level     
    def dif_input():    
        print("----------------------------")
        print("|Press 1 for Easy Mode     |")
        print("|Press 2 for Medium Mode   |")
        print("|Press 3 for Difficult Mode|")
        print("----------------------------")
        dif = int(input("Enter Your Choice: "))
        print()
        while dif != 1 and  dif != 2 and dif != 3 :
            dif = int(input("please enter '1'/'2'/'3': "))

        print("-------------------------")
        print("|press 'R' for 'ROCK'   |")
        print("|press 'P' for 'PAPER'  |")
        print("|press 'S' for 'SCISSOR'|")
        print("-------------------------")
        return dif

    # rock/paper/scissor by user
    def inputs():

        throw = input("ROCK-PAPER-SCISSOR: ")
        print()

        while throw != 'R' and throw != 'r' and throw != 'P' and throw != 'p' and throw != 'S' and throw != 's':
            throw = input("Please Press 'R'/'P'/'S': ")
            print()

        if throw == 'r' or throw == 'R':
            inpute = 'rock'
        elif throw == 'p' or throw == 'P':
            inpute = 'paper'
        else :
            inpute = 'scissor'

        print(f"You Have Chosen: '{inpute}'")
        return inpute

    # win/lose
    def winner(i,o):
        win = True
        if i == 'rock' and o == 'scissor':
            win 
        elif i == 'paper' and o == 'rock':
            win 
        elif i == 'scissor' and o == 'paper':
            win 
        elif i == o:
            win = None
        else:
            win = False
        return win


    #Main
    u_p = 0   #user points
    c_p = 0   #comp points
    print("------------------------------------")
    print("|Hello! Folks                      |")
    print("|Are You Ready To Test your luck in|")
    print("|_____ROCK - PAPER - SCISSOR_____  |")
    print("------------------------------------")
    print()


    level = dif_input()
    turns = 1
    while turns <= 5:
        print(f'{turns})',end=' ')
        throw_in = inputs()
        throw_out = pc_output(level,throw_in)
        win = winner(throw_in, throw_out)

        if win == True:
            u_p += 1
        elif win == None:
            u_p += 0
            c_p += 0
        else:
            c_p += 1

        turns += 1

    print(f"Your Score : PC Score = {u_p} : {c_p}")
    print()

    if u_p > c_p:
        print("----------")
        print("|YOU WIN!|")
        print("----------")
    elif c_p > u_p:
        print("-----------------------")
        print("|      You Loset!     |")
        print("|Better Luck Next Time|")
        print("-----------------------")
    else:
        print("-----------")
        print("|Its a TIE|")
        print("-----------")


# In[ ]:





# In[ ]:




