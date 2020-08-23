# 在本游戏中，每名玩家从牌堆中抽取一张牌，牌面点数最高的玩家获胜。我们将分别定义表示扑克牌、
# 牌堆、玩家和游戏的类，来逐步开发战争

from random import shuffle

## 扑克牌的类
class Card():
    suits = ["spades","hearts","diamonds","clubs"]
    values = [None,None,"2","3","4","5","6","7",
              "8","9","10","Jack","Queen","King","Ace"]

    def __init__(self,val,sui):
        """suit 和 value 的值均为整型数"""
        self.value = val
        self.suit = sui

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

## 牌堆的类
class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

## 表示玩家的类
class Player():
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name

## 表示游戏本身的类
class Game():
    def __init__(self):
        name1 = input("p1 name")
        name2 = input("p2 name")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        w = "{} wins this round".format(winner)

        print(w)

    def draw(self,p1n,p1c,p2n,p2c):
        d = "{} drew {} {} drew {}".format(p1n,p1c,p2n,p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "Enter q to quit or Enter y to continue"
            print(m)
            response = input("Pleas enter a key:")
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
                print("-" * 60)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
                print("-" * 60)

        win = self.winner(self.p1,self.p2)

        print(f"War is over. result is ({self.p1.name} : {self.p2.name} = {self.p1.wins}:\
{self.p2.wins}). so {win} wins")

    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game1 = Game()
game1.play_game()


