import time
import random

def main():
    print("Hi! Please enter the start state and the amount of H -> H transitions and T -> T transitions for the first 21 flips.")
    while True:
        try:
            init = str(input("Enter the start state: "))
            break
        except:
            print("That is not a valid option!")
    while True:
        try:
            a = int(input("Enter the amount of H -> H transitions for the first 21 flips: "))
            break
        except:
            print("That is not a valid option!")
    while True:
        try:
            b = int(input("Enter the amount of T -> T transitions for the first 21 flips:  "))
            break
        except:
            print("That is not a valid option!")

    steps = 10
    for i in range(steps+1): 
        print(init, end=", ")  
        rand = random.random() 
        if init == "H":
            if rand <= (a / 20):
                nextState = "H"
            else:
                nextState = "T"
        elif init == "T":
            if rand <= (b / 20):
                nextState = "T"
            else:
                nextState = "H"
        init = nextState

main()