import random

computer = random.randint(1, 3)
# 1 = Rock
# 2 = Paper
# 3 = Scissors

Player = str(input("Rock Paper Scissors "))
if Player == 'Rock' and computer == 3 or Player == 'Paper' and computer == 1 or Player == 'Scissors' and computer == 2:
    print("Player Wins")
else:
    print(computer)
    print("Computer Wins")
