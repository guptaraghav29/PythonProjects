import random

print("Hello!! What is your name?")
name = input()
print("\n" * 4)
print("Welcome " + name + " to \"THE GOAT's Rock, Paper, Scissors Game!\" ")
print()
print("Please choose between 'rock', 'paper', or 'scissors' and make sure the spelling is correct (lowercase letters please) !! ")
print("Type 'q' to quit the game!")

userInput = " "
userInput2 = " "

userCount = 0
cpuCount = 0
tieCount = 0

while userInput != "q" or userInput2 != "q":
    print()
    print()
    userInput = input(f"Enter your choice, {name}: ")

    if userInput == 'q':
        break

    cpu = random.randint(0, 2)
    if cpu == 0:
        userInput2 = "rock"
    elif cpu == 1:
        userInput2 = "paper"
    elif cpu == 2:
        userInput2 = "scissors"

    print()
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    print()
    print("SHOOT!")
    print()
    print("You chose: " + userInput)
    print("CPU chose: " + userInput2)
    print()

    if (userInput == userInput2) and ((userInput == 'rock' or userInput == 'paper' or userInput == 'scissors')):
        print("It's a tie!")
        tieCount += 1
    elif userInput == "rock" and userInput2 == "paper":
        print("CPU wins!")
        cpuCount += 1
    elif userInput == "rock" and userInput2 == "scissors":
        print("YOU win!")
        userCount += 1
    elif userInput == "paper" and userInput2 == "scissors":
        print("CPU wins!")
        cpuCount += 1
    elif userInput == "paper" and userInput2 == "rock":
        print("YOU win!")
        userCount += 1
    elif userInput == "scissors" and userInput2 == "paper":
        print("YOU win!")
        userCount += 1
    elif userInput == "scissors" and userInput2 == "rock":
        print("CPU wins!")
        cpuCount += 1
    else:
        print("Invalid input!!! Make sure you spell 'rock', 'paper', or 'scissors' with correct spelling in LOWERCASE!")

print()
print("Wow what great fun that was! Let's see that stats: ")
print(f"You won {userCount} times.")
print(f"The CPU won {cpuCount} times.")
print(f"CPU and you had {tieCount} ties.")
print()
print(f"Thanks {name} for playing the game, hope to see you again!!")
print()
