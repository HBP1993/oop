import random

# The Coin class simulates a coin that can
# be flipped.

class Coin: #name of the class Coin
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self): #initilization method
        self.sideup = 'Heads' #one object in defination attribute 
        #initialize with Head

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self): #anohter method self is parameter 
        if random.randint(0, 1) == 0: #its gonna pick a random number from range
            self.sideup = 'Heads' #if it is zero Head
        else:
            self.sideup = 'Tails' #if it is 1 Tail

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
            return self.sideup #return the value of the sideup
        
#this is a blueprint how to create the coin 
