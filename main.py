import random

def deal_card(): #function to pick a random card
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  print(card)
  
deal_card() #prints the function

user_cards = [] #user cards set to an empty list
computer_cards = [] #computer cards set to an empty list

for _ in range(0,1): #for loop used to pick 2 cards for the user
    user_cards.append(deal_card())
print(user_cards)