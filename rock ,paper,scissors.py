import time
ask = time.asctime(time.localtime(time.time()))
print(ask)
player1 = input("player 1 give your move")
player2 = input(" player 2 five your move")
if player1 =="rock" and player2 == "scissors":
    print("player 1 wins")
elif player1 == "paper" and player2 == "rock":
    print("player 1 wins")
elif player1 == "scissors" and player2 == "paper":
    print("player 1 wins")
elif player1 == player2:
    print("game is tie")
else:
    print("player 2 wins")
print(time.time())