class Towel:    #this
    def __init__(self, color: str, size: str): # constructor
        self.color: str = color # atributos
        self.size: str = size
        self.wetness: int = 0

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def isDry(self) -> bool:
        return self.wetness == 0
    
    def wringOut(self) -> None:
        self.wetness = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

    def __str__(self) -> str: # toString
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

def main(): #2
    toalha =  Towel("", "") # 3 objeto manipulado
    while True: #4 loop infinito
        line: str = input() # 5 entrada da linha
        args: list[str] = line.split(" ") # 6 lista de palavra
        
        print("$"+line)
        if args[0] == "end": # fim da execução 
            break 
        elif args[0] == "criar": # color 
            color = args[1]
            size = args[2]
            toalha =  Towel(color, size)
        elif args[0] == "mostrar":
            print(toalha)
        elif args[0] == "enxugar":
            amount: int = int(args[1])
            toalha.dry(amount) 
        elif args[0]== "seca":
            print("sim" if toalha.isDry() else "nao")
        elif args[0] == "torcer":
            toalha.wringOut()
        else: 
           print("fail: comando invalido")
main()