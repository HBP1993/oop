import CoinClass as c  # coin class is not the name class

# importing the name of the file not the class coin
# CoinClass is the name of the class


# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = (
        c.Coin()
    )  # this creates an instance called 'my_coin' of the class 'Coin()'
    # my_coin is a instinct of the class or object belongs to the coin class
    # all the method are avaliable to you to use the my_coin, you dont need to get Coin

    # Display the side of the coin that is facing up.
    print(
        "This side is up:", my_coin.get_sideup()
    )  # notice you do not have to supply the argument/parameter

    # Toss the coin.
    print("I am going to toss the coin ten times:")
    for count in range(10):
        my_coin.toss()
        # my_coin.sideup = "Heads" #this is not a good way to
        # use or get open access to other
        # the way we hide data attribute is two underscore __,
        # it doesn't tell user that you have a error rather gives simple regular result

        # Display the side of the coin that is facing up.
        print("This side is up:", my_coin.get_sideup())


# Call the main function.

main()
