import random
class Cards:
    def __init__(self):
        self.totalScore=300
        self.partialScore=0
        self.lost_points= 75
        self.win_points= 100
        self.previusNumber = 0
        self.currentNumber = 0

    def getTotalScore(self):
        return self.totalScore    
        
    def getPreviusCardNumber(self):
        # this function each time that is called return a 
        # random number(1 to 13)#
        self.previusNumber = random.randint(1, 13)
        return self.previusNumber

    def getCurrentCardNumber(self):
        # this function each time that is called return a 
        # random number(1 to 13)
        self.currentNumber = random.randint(1, 13)
        return self.currentNumber

    def getReadyPlayer(self):
        return self.player  

    def player_choice(self):
        print("The Magig Score is :", card.getTotalScore())
        #The player guesses if the next card will be higher or lower. (Julia)
        #getPreviusCardNumber entrega la carta anterior para la comparacion.
        print("The Card is : ",card.getPreviusCardNumber())
        opt = input("Higher or Lower [h/l] ? :")
        #getCurrentCardNumber entrega la carta posterior para la comparacion.
        self.currentNumber = card.getCurrentCardNumber()
        print("Next Card was : ",self.currentNumber)
        #Aca iria tu parte Julia############################
        #The player guesses if the next one will be higher or lower. (Julia)
        #The next card is displayed.(Julia)
     
card=Cards()
