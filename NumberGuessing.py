import random
while True:
    print("You will pick two numbers as a range to guess from. ")
    x = input("First number: ")
    y = input("Second number: ")
    z = random.randint(int(x), int(y))
    while True:
        p = int(input("Guess a number between " + x + " and " + y + " "))
        if p == z:
            c = input("Congratulations! Play again? Yes/No ")
            if c == "Yes":
                break
            elif c == "No":
                print("Bye.")
                exit(0)
            else:
                print("I don't understand.")
                exit(0)
        else:
            print("Wrong. Guess again. ")
            if z < p:
                print("The number is less than", p )
            else:
                print("The number is greater than", p)