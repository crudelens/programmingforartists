'''
2. class Fruit -> constructor (name [String], color[tuple], sweet[boolean]) three methods [ make Jam [returns boolean] name, color]
'''

class Fruit:
    def __init__(self, name:str, color:tuple, sweet:bool) -> None:
        self.name = name
        self.color = color
        self.sweet = sweet
        
    def getName(self):
        return self.name
             
    def getColor(self):
        return self.color
                
    def getSweet(self):
        return self.sweet

    def getMakejam(self):
        if self.sweet:
            return True
        else:
            return False