__author__ = 'lindsayhampton'

class Person(object):
    def __init__(self):
        self.name = ""
        print "Person Created"

    def gamble(self):
        pass

    def quit(self):
        pass

class Dealer(Person):
    def __init__(self):
        self.game_type = ""
        super(Dealer, self).__init__()
        print "Dealer Created"

    def deal(self):
        pass

class Player(Person):
    def __init__(self):
        self.bet = ""
        self.bank_roll = 100
        super(Player, self).__init__()
        print "Player Created"

    def hit(self):
        pass

    def stand(self):
        pass

class Card():
    def __init__(self):
        self.suit = ""
        self.value = 0
        print "Card Created"

class War(object):
    def __init__(self):
        print "Game Created"
        card = Card()
        card.suit = "Clubs"
        card.value = 7
        print str(card.value) + " of " + card.suit

game = War()
