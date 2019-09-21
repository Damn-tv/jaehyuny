nuclearwating = -1
import random
class minseong:

    def __init__(self):
        self.hp = random.randrange(250, 300)
        self.mp = random.randrange(40, 50)
        self.atk = random.randrange(30, 50)

    def attack(self):
        return self.atk


    def defend(self, damage):
        self.mp = self.mp + random.randrange(20, 40)
        if(c == 1):
            self.hp = self.hp - damage
            print('일반공격을 시전하엿다!')
        elif(c == 2):
            self.Feedback()
            print('환류를 시전하엿다!')
        elif(c == 3):
            self.nuclear()
            print('핵공격이 감지되엇습니다')


    def nuclear(self):
        print('사용자는 3턴간 움직이지 못하며 3턴뒤 폭*파 합니다')

    def Feedback(self):
        self.mp = self.mp - self.mp/2
        if (turn == 0):
            player2.hp = player2.hp - player2.mp
            player2.mp = 0
        if (turn == 1):
            player1.hp = player1.hp - player1.mp
            player1.mp = 0

    def see_hp1(self):
        return self.hp


player1 = minseong()
player2 = minseong()
turn = 0
while(player1.hp > 0 or player2.hp > 0):
    print("player1 hp", player1.hp, "          player2 hp", player2.hp)
    print("player1 mp", player1.mp, "          player2 mp", player2.mp)
    print("player1 atk", player1.atk, "          player2 atk", player2.atk)
    if(turn == 0):
        c = int(input('enter the number(plater1 turn)(1, attack)'))
        if(c == 1):
            print("Selct attck")
            d = player1.attack()
            player2.defend(d)

        elif(c == 2):
            print('select attatck')
            d = player1.attack()
            player1.defend(d)
        turn = 1

    else:
        c = int(input('enter the number(plater2 turn)(1, attack)'))
        if (c == 1):
            d = player2.attack()
            player1.defend(d)
            turn = 0
        elif(c == 2):
            d = player2.attack()
            player1.defend(d)
            turn = 0
        elif(c == 3):
            d = player2.attack()
            player1.defend(d)
            turn = 0


