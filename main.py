import random

def deal_card(): #function to pick a random card...............................1
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card #prints ANY number from the list
  
def calculate_score(cards): #....................................................2
    """Take a list of cards and return the score calculated from the cards"""
    if sum in cards == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

user_cards = [] #user cards set to an empty list
computer_cards = [] #computer cards set to an empty list
is_game_over = False

for _ in range(2): #for loop used to pick 2 cards, 1 for user and 1 for computer.......3
    user_cards.append(deal_card()) #for the user
    computer_cards.append(deal_card()) #for the computer
print(user_cards)
print(computer_cards)

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f" Your cards {user_cards}, current score: {user_score}")
print(f" Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
else:
    question = input("Type yes to get another card or no, to pass ").lower()
    if question == "yes":
        user_cards.append(deal_card())
        print(user_cards)
    else:
        is_game_over = True
