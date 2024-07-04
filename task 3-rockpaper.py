import random

print("Welcome to rock paper scissors game")
user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name: ")
print("""
Winning rules:
1. paper vs rock --> paper wins
2. rock vs scissors --> rock wins
3. scissors vs paper --> scissors wins
""")

while True:
    print("Choices are:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = int(input("Enter your choice (1-3): "))
    print()

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input (1-3): "))
        print()

    if choice == 1:
        user_choice = "rock"
    elif choice == 2:
        user_choice = "paper"
    else:
        user_choice = "scissors"

    print("Your choice is:", user_choice)
    print("Now it's computer's turn...")

    computer = random.randint(1, 3)
    if computer == 1:
        comp_choice = "rock"
    elif computer == 2:
        comp_choice = "paper"
    else:
        comp_choice = "scissors"

    print("Computer's choice is:", comp_choice)

    if (user_choice == "paper" and comp_choice == "rock") or \
       (user_choice == "rock" and comp_choice == "scissors") or \
       (user_choice == "scissors" and comp_choice == "paper"):
        print(user_choice.capitalize(), "wins!")
        user_score += 1
    elif user_choice == comp_choice:
        print("It's a tie!")
        ties += 1
    else:
        print(comp_choice.capitalize(), "wins!")
        comp_score += 1

    print("\nScores:")
    print(name + "'s score:", user_score)
    print("Computer's score:", comp_score)
    print("Ties:", ties)

    repeat = input("Do you want to play again? (yes/no): ")
    if repeat.lower() != "yes":
        break

print("\nGame over!")
print("Thanks for playing!")