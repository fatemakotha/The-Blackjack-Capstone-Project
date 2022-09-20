import random #imports the random function

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #this is the deck available, 11 is an ACE

def deal_card(): #this function chooses one card randomly
    chosen_card = random.choice(cards)
    print(chosen_card)
deal_card() #calls the funtion
