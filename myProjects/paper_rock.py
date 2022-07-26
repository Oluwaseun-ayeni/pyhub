player_1 = input("P1 enter your name: ")
player_2 = input("P2 enter your name: ")

print("Welcome to rocks game " + player_1 + ' and ' + player_2)

choice = ['paper', 'scissor', 'rock']

while True:

    player_1_choice = input(player_1 + " ,enter your code ")

    player_2_choice = input(player_2 + " ,enter your code ")

    if player_1_choice and player_2_choice not in choice:
        print("invalid code")
        continue
    if player_1_choice or player_2_choice != "exit ":
        print("Start")

        if player_1_choice == player_2_choice:

            print("game tied motherfuckers")
            continue

        elif player_1_choice == 'rock' and player_2_choice == 'paper':
            print(player_1 + " ,Wins")
            continue
        elif player_2_choice == 'rock' and player_1_choice == 'paper':
            print(player_2 + " ,Wins")
            continue

        elif player_1_choice == 'scissor' and player_2_choice == 'paper':
            print(player_1 + " ,Wins")
            continue
        elif player_2_choice == 'scissor' and player_1_choice == 'paper':
            print(player_2 + " ,Wins")
            continue

        elif player_1_choice == 'scissor' and player_2_choice == 'rock':
            print(player_2 + " ,Wins")
            continue

        else:
            print(player_1 + "Wins")
