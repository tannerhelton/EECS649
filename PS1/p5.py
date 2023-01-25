import time
import random

def countMag(num):
    zeros = 0
    while num > 0:
        zeros += 1
        num = num // 10
    return zeros
        
def addInts(a, b):
    sum = a + b
    aDig = countMag(a)
    bDig = countMag(b)
    digits = aDig if aDig < bDig else bDig
    if digits < 2:
        time.sleep(random.randint(1, 2))
    elif digits < 4:
        time.sleep(random.randint(1, 3))
    elif digits < 6:
        time.sleep(random.randint(1, 7))
    elif digits < 8:
        time.sleep(random.randint(3, 9))
    elif digits < 10:
        time.sleep(random.randint(6, 14))
    elif digits < 12:
        time.sleep(random.randint(9, 18))
    elif digits < 14:
        time.sleep(random.randint(15, 22))
    else:
        time.sleep(random.randint(17, 25))

    if random.random() < 0.5:
        sum = sum * 1.1 if random.random() < 0.5 else sum * 0.9
    return int(round(sum, 0))

def main():
    print("Hello user, please enter two integers on two separate lines. These will be sent to a correspondent to sum.")
    while True:
        try:
            a = int(input("Enter the first integer: "))
            break
        except:
            print("That's not a valid option!")
    while True:
        try:
            b = int(input("Enter the second integer: "))
            break
        except:
            print("That's not a valid option!")
    print("The sum of the two integers is... ")
    print(addInts(a, b))

main()