
class PartyAnimal:
  # Class parameteres
  x = 0
  name = ""
  # Class methods (i.e. functions)
  def __init__(self,person):   # self is the instance of the class, z is the first argument passed
    self.name = person
    print('Constructed',self.name)

  def party(self):
    self.x=self.x + 1
    print(self.name,"party count:",self.x)

  def __del__(self):
    print(self.name,'destructed. Last value of',self.x)

sally = PartyAnimal("Sally")
jim = PartyAnimal("Jim")

print('')
sally.party()
jim.party()
jim.party()
print('')