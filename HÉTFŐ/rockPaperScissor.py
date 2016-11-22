import random


def get_ai_number():
    ai_number = 0
    ai_number = random.randint(1, 4)
    return ai_number


def get_player_number():
    player_number = ""
    try:
        player_number = input("Rock paper or scissor?")
        player_number = player_number.lower()
        if player_number == "rock":
            player_number = 1
        if player_number == "paper":
            player_number = 2
        if player_number == "scissor":
            player_number = 3
    except ValueError:
        print("please only enter rock paper or scissor")
    return player_number


def gameplay(num1, num2):
    if num1 == 1 and num2 == 3:
        print("The AI wins!")
        print("You chose scissor, the ai chose rock!")
    if num1 == 2 and num2 == 3:
        print("The player wins!")
        print("You chose scissor, the ai chose paper!")
    if num1 == 3 and num2 == 3:
        print("Draw!")
    if num1 == 1 and num2 == 2:
        print("The player wins!")
        print("You chose paper, the ai chose rock!")
    if num1 == 2 and num2 == 2:
        print("Draw!")
    if num1 == 3 and num2 == 2:
        print("The AI wins!")
        print("You chose paper, the ai chose scissor!")
    if num1 == 1 and num2 == 1:
        print("Draw!")
    if num1 == 2 and num2 == 1:
        print("The AI wins!")
        print("You chose rock, the ai chose paper!")
    if num1 == 3 and num2 == 1:
        print("The player wins!")
        print("You chose rock, the ai chose scissor!")


def main():
    while True:
        gameplay(get_ai_number(), get_player_number())

main()
