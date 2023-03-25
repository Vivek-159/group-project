import Guess
import RPS
import tic_tac_toe

print("                                 ------------------------------")
print("                                 | __________HELLO!__________ |")
print("                                 | _____WELCOME TO ARCADE____ |")
print("                                 ------------------------------")
print()


print("                           -----------------------------------------------")
print("                           | Press '1' To Play 'FIND THE WORD'           |")
print("                           | Press '2' To Play 'ROCK - PAPER - SCISSORS' |")
print("                           | Press '3' To Play 'TIC - TAC - TOE'         |")
print("                           | Press '4' To EXIT                           |")
print("                           -----------------------------------------------")

i = int(input("                                        Your Choice: "))
print()
while i != 1 and i != 2 and i != 3 and i != 4:
    i = int(input("Please Press '1'/'2'/'3'/'4' : "))
    print()
 
print("-----------------------------------------------------------------------------------------------------------------")
    
while i != 4:
    if i == 1:
        Guess.find_the_word()
        print("-----------------------------------------------------------------------------------------------------------------")
    elif i == 2:
        RPS.rock_paper_scissor()
        print("-----------------------------------------------------------------------------------------------------------------")
    else:
        tic_tac_toe.mark = 'X'
        tic_tac_toe.tic_tac_toe()
       
        print("-----------------------------------------------------------------------------------------------------------------")

        
    i = int(input("Please Press '1'/'2'/'3'/'4' To 'Continue Playing' or 'Exit' : "))
    while i != 1 and i != 2 and i != 3 and i != 4:
        i = int(input("Please Press '1'/'2'/'3'/'4' : "))
        print()
    
print("                                      -----------------------")       
print("                                      | Thanks For Playing. |")
print("                                      |  Hope you Enjoyed.  |")
print("                                      -----------------------")