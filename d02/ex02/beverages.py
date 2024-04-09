class HotBeverages:
  def __init__(self, price = 0.30, name = "hot beverages", description = "Just some hot water in a cup."):
    self.price = price
    self.name = name
    self.description = description

  def __str__(self):
    return f"name: {self.name}\nprice: {self.price:.2f}\ndescription: {self.description}"

class Coffee(HotBeverages):
  def __init__(self):
    super().__init__(0.40, "coffee", "A coffee, to stay awake.")

class Tea(HotBeverages):
  def __init__(self):
    super().__init__(name = "tea")

class Chocolate(HotBeverages):
  def __init__(self):
    super().__init__(price = 0.50, name = "chocolate", description="Chocolate, sweet chocolate...")

class Cappuccino(HotBeverages):
  def __init__(self):
    super().__init__(price = 0.45, name = "cappuccino", description="Un po' di Italia nella sua tazza!")

def main():
  drinks = (HotBeverages(), Coffee(), Tea(), Chocolate(), Cappuccino())
  for drink in drinks:
    print(drink)
    print("")



if __name__ == "__main__":
  main()
