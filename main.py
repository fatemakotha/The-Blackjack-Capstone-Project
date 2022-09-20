import random

def deal_card(): #function to pick a random card
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  print(card)
  
deal_card()#prints the function

user_cards = []#user cards set to an empty list

