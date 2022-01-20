import random, os

class Player_:    
    def __init__(self) :
        self.score=300
        #print(self.score)
        
class Director:    
    def __init__(self):
        self.isPlaying = True
        self.cards=[]
        self.o=""
        
        for i in range(13):
            player = Player_()#instancio clase Cards
            self.cards.append(player)
            
           # print("--------------------------------------------------")
           # print(f"Position in memory of card {i} \n{self.cards}\n") 
            
    def runPlay(self):
        self.o = input("Do yo Start Playing ? y/n : ")    
        if self.o=="y":
            director.isPlaying=True
            return self.isPlaying
        else:
             director.isPlaying=False
             return self.isPlaying
         
    def show_score(self):
        print("-----------------------------------------------")
        print(f"Player 1 Starting Score : {player.score}  ")    
    
    def getReadyCards(self):
        random.shuffle(self.cards)
        n = random.randint(1, 13)
        print(f"The card is  {n}")    
    
        
j=""        
director= Director()

while director.isPlaying:
    director.isPlaying = director.runPlay()
    director.getReadyCards()
    player = Player_()
    print(f"Score : {player.score}")
    
    
else:
    print("Thank you!")    
