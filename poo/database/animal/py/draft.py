class Animal:
    def __init__(self, species: str, sound: str,): # constructor
      self.species: str = species
      self.sound: str = sound
      self.age: int = 0
     
    def __str__(self):
       return f"{self.species}:{self.age}:{self.sound}"
    
def main():
   animal: Animal = Animal("", "")
   while True:
      line = input()
      print("$" + line)
      args = line.split(" ")

      if args[0] == "end":
         break
      elif args[0] == "init":
         species = args[1]
         sound = args [2]