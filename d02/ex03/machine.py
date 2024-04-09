import random as rnd
from beverages import *

class Coffeemashine:
  def __init__(self):
    self.drinks_served = 0
    self.drinks = (Coffee(), Tea(), Chocolate(), Cappuccino())

  class EmptyCup(HotBeverages):
    def __init__(self):
      super().__init__(price = 0.90, name = "empty cup")

    def description(self):
      return "An empty cup?! Gimme my money back"

  class BrokenMachineException(Exception):
    def __init__(self):
      super().__init__("This coffee mashine has to be repaired.")

  def repair(self):
    self.drinks_served = 0

  def serve(self, input_drink: HotBeverages):
    for drink in self.drinks:
      if drink.description() == input_drink.description() and self.drinks_served < 10:
        self.drinks_served += 1
        choice = rnd.randint(1, 10)
        if choice > 5:
          return (drink)
        else:
          return (self.EmptyCup())
    raise self.BrokenMachineException()

def main():
  try:
    mashine = Coffeemashine()
    for i in range(0, 10):
      if i % 2 == 0:
        print(mashine.serve(Coffee()))
        print()
      else:
        print(mashine.serve(Tea()))
        print()
    mashine.serve(Chocolate())
  except Exception as e:
    print(e)

  try:
    mashine.serve(Chocolate())
  except Exception as e:
    print(e)

  try:
    mashine.repair()
    print()
    print(mashine.serve(Cappuccino()))
  except Exception as e:
    print(e)

if __name__ == "__main__":
  main()
