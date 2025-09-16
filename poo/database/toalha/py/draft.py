
class Towel: 
    def __init__(self, color: str, size: str): # construtor 
        self.color = "red" # atributos
        self.size = "p"
        self.wetness = 0

    def __str__(self):
        return f"color:{self.color}, tam:{self.size}, hum{self.wetness}"




towel = Towel(" green", "G") #objetos
toalha = Towel("red", "p")
outra = toalha
print(towel.color)
print(towel.color)
print(towel.size)
print(towel.wetness)       