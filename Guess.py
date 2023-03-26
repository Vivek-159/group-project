#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
def find_the_word():
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']

    word = random.choice(words)

    user_input = ''

    print("-------------")
    print("|Hello! Folks|")
    print("-------------")
    print()
    print("----------------------------")
    print("|Welcome To 'Find The Word'|")
    print("----------------------------")
    print()

    print("Rules are simple:")
    print("----------------------------------------------------------------------------")
    print("|There Is A 'SECRET WORD'.                                                  |")
    print("|You Have To Guess A Letter Of The 'SECRET WORD' One At A Time.             |")
    print("|If The Letter Is In The 'SECRET WORD', You Procede Without Losing Turns.   |")
    print("|But If You Guess It Wrong, You Lose '1' Turn.                              |")
    print("|If You Find The 'SECRET WORD' Befor Losing Your All Turns, You 'WIN'.      |")
    print("----------------------------------------------------------------------------")
    print()

    print("---------------------------------")
    print("|Choose the level of difficulty.|")
    print("|Press '1' for 'Easy Mode'      |")
    print("|Press '2' for 'Hard Mode'      |")
    print("---------------------------------")
    level = int(input("Your Choice: "))

    while level != 1 and level != 2:
        print("Please Press '1' or '2'.")
        level = int(input("Your Choice: "))

    if level == 1:
        dif = 'Easy'
        turns = 6
    else:
        dif = 'Hard'
        turns = 3

    print("---------------------------")
    print(f"|You Have chosen {dif} Mode|")
    print("---------------------------")

    print()

    print("ALRIGHT")
    print("LET'S")
    print("BEGIN")
    print()

    lenw = len(word)
    print(f"---------------------------------------")
    print(f"|Guess a '{lenw}' Letter Word              |")
    print(f"|You Have Total Of '{turns}' Turns.         |")
    print(f"|your 1st letter is " + "'" + word[0]  + "'" +  f" and {lenw}th is " + "'" +  word[lenw-1] +  "'|" )
    print(f"---------------------------------------")

    while turns > 0:
        guess = input('Enter A Letter: ')
        if guess in word:
            print("Correct Guess")
            print()
        else:
            print("Oops! Try Again")
            turns -= 1
            print(f"You Have {turns} turns Left")
            print()


        user_input += guess
        flag = 0
        for letter in word:
            if letter in user_input:     
                print(letter,end='')     
            else:
                print('_',end='')
                flag += 1
        print()
        if flag == 0:
            print("\n\n\n")
            print("------------------------------")
            print("|Great You Won               ")
            print(f"|The 'SECRET WORD' Is: {word}")
            print("------------------------------")
            break
    else:
        print("\n\n\n")
        print("-----------------------")
        print("|You Lost!            |")
        print("|Better Luck Next Time|")
        print("-----------------------")


# In[ ]:




