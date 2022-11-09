import random

class Cards:
    def __init__(self):


        self.ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        self.suits = ["Spades", "Hearts", "Clubs","Diamonds"]
        self.deck = []
    def flip(self):
        value = 1
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append([rank + " of " + suit, value])
            value = value + 1

        random.shuffle(self.deck)
        score = 300
        card1 = self.deck.pop(0)

        value = random.shuffle(self.deck)
        self.points = print("Your score so far is", score)
        print("The current card is", card1 [0])

        self.choice = input ("higher or lower?")



        card2 = self.deck.pop(0)
        print("the next card is", card2[0])



        if self.choice =="higher" and card2[1] > card1[1]:
            score += 100
        elif self.choice =="lower" and card2[1] < card1[1]:
            score += 100
        elif self.choice =="higher" and card2[1] == card1[1]:
            self.score += 0
        elif self.choice =="lower" and card2[1] == card1[1]:
            score += 0
        else:
            score -= 75
        card1 = card2
