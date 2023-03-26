import random
mark = 'X'
winner = None
def tic_tac_toe():
    
    bord = ['-','-','-','-','-','-','-','-','-']
    # print the bord
    def printbord(bord):
        print(bord[0] +'|'+bord[1] +'|'+bord[2])
        print("-----")
        print(bord[3] +'|'+bord[4] +'|'+bord[5])
        print("-----")
        print(bord[6] +'|'+bord[7] +'|'+bord[8])

    # switch between players 
    def switchplayer():
        global mark
        if mark == 'X':
            mark = 'O'
        else:
            mark = 'X'



    # check winner or tie
    def checkwinner(bord):
        global winner
        # horizontal
        if bord[0] == bord[1] == bord[2] != '-':
            winner = bord[0]
            return True

        elif bord[3] == bord[4] == bord[5] != '-':
            winner = bord[3]
            return True

        elif bord[6] == bord[7] == bord[8] != '-':
            winner = bord[6]
            return True

        # digonal
        elif bord[0] == bord[4] == bord[8] != '-':
            winner = bord[0]
            return True

        elif bord[2] == bord[4] == bord[6] != '-':
            winner = bord[2]
            return True

        # vertical
        elif bord[0] == bord[3] == bord[6] != '-':
            winner = bord[0]
            return True

        elif bord[1] == bord[4] == bord[7] != '-':
            winner = bord[1]
            return True

        elif bord[2] == bord[5] == bord[8] != '-':
            winner = bord[2]
            return True


    def checktie(bord):
        global gameon
        if '-' not in bord:
            return True


    # input by player
    def inputplayer(bord):
        i = int(input("Enter Number Between 1-9: "))
        print()

        while i < 1 or i > 9 or bord[i-1] != '-':
            if i < 1 or i > 9 :
                i= int(input("Enter Number Between 1-9: "))
                print()
            else:
                i = int(input("Oops! already filled press something else:"))

        bord[i-1] = mark
        printbord(bord)
        print()
        switchplayer()

    def withcomp(bord):
        if checkwinner(bord) == True:
            return 'win'
        if checktie(bord) == True:
            return 'tie'

        while mark == 'O':
            i = random.randint(0,8)
            while bord[i] != '-':
                i = random.randint(0,8)
            bord[i] = 'O'
            printbord(bord)
            print()
            switchplayer()


    '''-----------------------------------------------------------------------------------'''
    # main

    print("--------------")
    print("|HELLO FOLKS!|")
    print("|Lets Play   |")
    print("|TIC-TAC-TOE |")
    print("--------------")

    printbord(bord)

    print()
    print("------------------------------------")
    print("|Press '1' To Play With 'Computer'.|")
    print("|Press '2' To Play With a 'Friend'.|")
    print("------------------------------------")

    inp = int(input("Your Choice: "))
    while inp != 1 and inp != 2:
        inp = int(input("Press '1' or '2': "))
    print()

    print('1' + '|' + '2' + '|' + '3')
    print("-----")
    print('4' + '|' + '5' + '|' + '6')
    print("-----")
    print('7' + '|' + '8' + '|' + '9')
    print()

    while 1:
        inputplayer(bord)

        print()
        if inp == 1:
            comp = withcomp(bord)
            if comp == 'win' or comp == 'tie':
                break

        if checkwinner(bord) == True:
            break

        if checktie(bord) == True:
            break


    if winner != None:
        print("-----------------")
        print(f"|Player '{winner}' win!|")
        print("-----------------")
        #mark = 'x'
    else:
        print("-----------")
        print("|Its a tie|")
        print("-----------")
mark = 'X' 
winner = None
