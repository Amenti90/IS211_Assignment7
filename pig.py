import random

players= []

score_count = 0


class Player:

    def __init__(self):
        self.score_count = 0

    def turn (self):
        players= []
        avatar = input("What is your name?: ")
        players = players + avatar

        for i in players:
            print (i)

        go= input("Would you like to 'roll' or 'hold'? ")
        if go == 'hold':
            print (self.score_count)
        else:
            while self.score_count < 100:
                x = random.randint(1, 6)
                y = x + self.score_count
                print(x)
                print("Your score is : ")
                print(y)
                continue







#class Game:
if __name__=="__main__":
    for i in players:
        Player()







