import random

def main():
    question = "capital"
    anwser = "state"
    lives = 3
    score = 0
    gameOver = False;
    f = open("states.txt", "r");
    states = []
    for state in f:
        splitState = state.split(", ")
        states.append({"capital":splitState[0],"state":splitState[1].removesuffix("\n")})
    f.close()

    mode = input("Guess state(S) or capital(C): ")

    if  mode.__eq__('C') or mode.__eq__('c' or mode.__eq__('capital')):
        question = "state"
        anwser = "capital"

    while len(states)>0 and not(gameOver):
        num = random.randint(0,len(states)-1)
        userAnwser = input("What is the "+anwser+" of "+states[num].get(question)+": ")
        if(userAnwser.lower() == states[num].get(anwser).lower()):
            print("Correct")
            score = score+1
            states.pop(num)
        else:
            print("Incorrect! Anwser was "+states[num].get(anwser))
            lives = lives - 1
            print("Lives: "+str(lives))
            if(lives==0):
                gameOver = True
    print("Final Score: " + str(score))







if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
