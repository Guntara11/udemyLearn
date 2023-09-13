import random

highest = 10 
answer = random.randint(1, highest)

print("please guess number between 1 and {}".format(highest))

guess = int(input())

if guess == answer:
    print ("you got it first time")
else:
    if guess < answer: 
        print("please guess higher")
    else:
        print("please guess lower")
    guess = int(input())
    if guess == answer:
        print ("well done")
    else:
        print("sorry, maybe next time ")