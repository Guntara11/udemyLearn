low = 1 
high = 1000

print("please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1 

while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower"
                     "Enter h or l or c if my guess was correct "
                     .format(guess)).casefold()
    if high_low == "h":
        low = guess + 1 
        # GUESS higher. the low end of the range becomes 1 greater than the guess
    elif high_low == "l":
        high = guess - 1 
        # GUESS lower, the high end of the range becomes 1 lower than the guess 
    
    elif high_low == "c":
        print("I got it in {} guesses!!".format(guess))
    else:
        print("Please enter h, l, or c ")

