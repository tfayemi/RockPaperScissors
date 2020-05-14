from random import randint as rand

#create play options 
t = ["Rock", "Paper", "Scissors"]

#Giving the computer a random play option
computer = t[rand(0,2)]

#set play to False
player = False
print("LET'S PLAY ROCK - PAPER - SCISSORS!!!\n")
print("a python game by AngelaGames™\n")
print("***************NEW GAME***************")
while player == False:
  #set player to True
  player = input("Rock, Paper, Scissors???:\n")
  print("Computer Picked", computer)
  if player == computer:
    print("Tie!!")
  elif player == "Rock":
    if computer == "Paper":
      print("You lose!", computer, "covers", player)
    else:
      print("You beat me!", player, "smashes", computer)
  elif player == "Paper":
      if computer == "Scissors":
          print("You lose!", computer, "cut", player)
      else:
          print("You win!", player, "covers", computer)
  elif player == "Scissors":
      if computer == "Rock":
          print("You lose...", computer, "smashes", player)
      else:
          print("You win!", player, "cuts", computer)
  else:
    print("Invalid input!!! Try again")

  print("\n Wanna play again? \n")
  
  player = False
  computer = t[rand(0,2)]

