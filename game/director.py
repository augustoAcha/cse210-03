
class Director:
    
    def __init__(self):
        print("estoy en el init del Director")
        self.dice=[]
        self.isPlaying=True
            
    
    def startgame(self):
        print("Estoy dentro de startgame")
        while self.isPlaying:
          print("inside While loop..")

          o = input("Do you Play  y / n ?")

          if o != "y":
              self.isPlaying = False



