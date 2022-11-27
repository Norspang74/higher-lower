### Package import ###
from replit import clear
from random import randint
import art
import game_data

### Global Variables ###
first_data = randint(0,len(game_data.data)-1)
second_data = 0
goon = True
score = 0
### Funcktions ###
def print_data(list_nr):
  print(f"{game_data.data[list_nr]['name']} is a {game_data.data[list_nr]['description']} from {game_data.data[list_nr]['country']}")
  return game_data.data[list_nr]['follower_count']

### Program ###
while goon:
  clear()
  print(art.logo)
  if score > 0:
    print (f"Your score is {score}.")
  else:
    print ("")
  print("Campare A:")
  folowers_a = print_data(first_data)
  print(art.vs)
  print("Against B:")
  second_data = randint(0,len(game_data.data)-1)
  folowers_b = print_data(second_data)
  guess = input("Who has more folowers? A or B: ")
  result = "A" if folowers_a > folowers_b else "B"
  if result == guess.upper():
    score += 1
    first_data=second_data
    goon =True
  else:
    clear()
    print(art.logo)
    print(f"Sorry, that was wrong. Final score: {score}")
    goon = False
