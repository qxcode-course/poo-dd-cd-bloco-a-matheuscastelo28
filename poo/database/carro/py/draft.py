class Carro: 
    def __init__(self):
        self.passageiro = 0
        self.gas = 0
        self.km = 0
        self.passMax = 2
        self.gasMax = 100

    def enter(self):
        if self.passageiro < self.passMax:
            self.passageiro +=1 
        else:
            print("fail: limite de pessoas atingido")

        
    def leave(self):
        if self.passageiro > 0:
            self.passageiro -=1
        else:
            print("fail: nao ha ninguem no carro") 
    
    def fuel(self, qnt:int):
        self.gas += qnt
        if self.gas > self.gasMax:
            self.gas = self.gasMax
            
    def drive(self, dist : int):
        if self.passageiro == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if dist <= self.gas:
            self.gas+= dist
            self.km-= dist
        else :
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas
            self.gas = 0
        
        
    def __str__(self):
        return f"pass: {self.passageiros}, gas: {self.gas}, km: {self.km}"
    
def main():
      carro = Carro()
      while True:
        line : str = input()
        args:list[str] = line.split()
        print("$"+line)

        if args[0] == "end":
             break 
        elif args[0] == "show":
             print(carro)

        elif args[0] == "enter":
             carro.enter()
             
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            carro
      

            