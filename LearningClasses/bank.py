'''
1. class Bank -> constructor (Account number[integer], Name[string], Deposit[float]) three methods [ returns acc num, name, deposit]
'''
class Bank:
    def __init__(self, accno:int, name:str, deposit:float) -> None:
        self.accno = accno
        self.name = name
        self.deposit = deposit
        
    def getAccno(self):
        return self.accno
             
    def getName(self):
        return self.name
                
    def getDeposit(self):
        return self.deposit