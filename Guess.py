import random
turn = 1
score = 0
first = 0
one = ""
i = 1
noPlay = False

def firstTime(first):
    if first == 0:
        print("\nType a number between 1 and 3 and guess the random number")
    one = input("Guess: ")
    return one

def res(z, y):
    res = (z/y)*100
    return res

def end(what, turn, score):
    play = False
    while True:
        if what == "Y":
            print("\nHere we go again!!!")
            turn = 1
            score = 0
            break
        elif what == "N":
            print("\nYou killed me, see what you did?")
            play = True
            break
        else:
            print("\nThat is not a very clear answer, ya know?")
            what = input("Repeat -.-\n>>>").upper().replace("[" or "]", "", 2)
    return play

def converter(into):
    try:
        i = int(into)
        return i
    except:
        print("\nThat is not a number")
        return

def turnCount(turn):
    turn += 1
    return turn

def calc(into, score, turn):
    x = random.randint(1,3)
    i = converter(into)
    if i:
        if i <= 3 and i >= 1:
            if i == x:
                print("\nCorrect")
                score += 1
            else:
                print("\nWrong\nIt was {}".format(x)) 
            turnCount(turn-1)
        else:
            print("\nType a number between 1 and 3")
    return score

while True:
    score = calc(firstTime(first), score, turn)
    first = 1
    turn = turnCount(turn)
    if turn == 10:
        two = input("\nYou were correct {} percent of the time\n\nIf you want to continue, type [Y] else type [N]\n>>>".format(res(score, turn))).replace("[", "").replace("]", "").upper()
        noPlay = end(two, turn, score)
        turn = 0
        score = 0
        if noPlay:
            break