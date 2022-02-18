"""
Playing Cards

We ask you to design a card game using the traditional 52-card deck. We divide theis question
in to three parts, so you can complete them in order.

Part One

For this first part, you must design a Game class representing the game, and these following 
functions associated with the class.

-add_card(suit, value): Creates a new card object with a suit from one of the following strings
Hearts, Spades, Clubs, Diamonds, and a value from one of the following strings: A, 2-10,J,Q,K.
This card is represented by i, where i is an integer indicating how many cards have been 
created before.
-card_string(card): Returns the string representation of the card represented by i. It follows
the format <value> of <suit>. For example, a card created by add_card("Spades", "3") should
have a string representation of 3 of spades.
-card_beats(card_a, card_b): Check if the card represented by card_a beats the one represented
by card_b. A card beats another card if and only if it has a greater value. The value of the 
cards are ordered from A to K.
You may implement these however you like. However preferably this should be easily expandable
to accomodate new requirements.


"""
class Game:

    def __init__(self):
        # Implement initializer here
        pass

    def add_card(self, suit: str, value: str)->None:
        # Implement function here
        pass

    def card_string(self, card:int)->str:
        # Implement function here
        return ""

    def card_beats(self, card_a:int, card_b:int)->bool:
        # implement function here
        return False

if __name__=='__main__':
    pass

"""
Solution

There are numerous approach we can take to design this problem. The sample solution will
provide an object-oriented approach, since it allows us to easily add new types of cards to
accomodate new requirements.

Different languages have different tools,  but the basic concept in object oriented programming
is inheritance, which is a class deriving from a superclass and inheriting  its methods.
In this situation, a playing card from the 52 is a card. The reason for this design is that
we can easily add other types of cards if we want.

"""


"""
Part Two
For this part, we ask you to implement the Jokers into the system.

In addition, to the functionalities above, also implement the following functions:

add_joker(color): Creates a Joker card of with color of either Red or Black.
    - Joker beats everything else except other jokers. This card is represented by i, where i
    is an integer indicating how many cards have been created before, including both normal 
    cards and jokers.
    - A joker's string representation is Red Joker or Black Joker, depending on the color.


Solution

We add a Joker class that inherits the base card. For the purpose of this question, its value
is 14, which is greater than other cards. We do not need to write extra logic for comparing 
Jokers with other cards, since that logic is already under Card.

Below is the updated implementation.
"""




"""
Part Three

This game also involve a concept of a Hand and comparing the sie of the two hands. For this
part, add these following functions to the Game class:

-add_hand(card_indices): Create a new Hand with cards represented by the list of integer
representation of cards card_indices. The hand can be represented by i, where i is the number
of hands added before.
-hand_string(hand): Return the string representation of the hand represented by hand. It is
a list of string representation of  cards by their insertion order, seperated by ", ". For 
example, if hand has a 9 of Clubs, K of Hearts, and a Black Joker, the string representation
is "9 of clubs, K of Hearts, Black Joker".
-beats_hand(hand_a, hand_b): Check if the hand represented by hand_a beats the hand represented 
by hand_b according to the following rules:
    - Starting from the largest card in each hand, compare them. If a card beats another, that
    hands bests the other hand.Otherwise, compare the next largest card.
    - Repreat this process until one hand beats the other, or one hand runs out of cards. If a
    hand runs out of cards. If a hand runs out of cards, neither hand beat each other.


Solution
For this part, we implement the Hand class by having it contain a list of cards. When we compare 
two hands, because we defined a comparison function between two cards, we can sort them using the
default sorting algorithm

Below is the implementation
"""