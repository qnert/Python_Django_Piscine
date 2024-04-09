class HotBeverages:
  def __init__(self, price = 0.30, name = "hot beverages"):
    self.price = price
    self.name = name

  def __str__(self):
    return f"name: {self.name}\nprice: {self.price:.2f}\ndescription: {self.description()}"

  def description(self):
    return "Just some hot water in a cup."

class Coffee(HotBeverages):
  def __init__(self):
    super().__init__(0.40, "coffee")

  def description(self):
    return "A coffee, to stay awake."

class Tea(HotBeverages):
  def __init__(self):
    super().__init__(name = "tea")

  def description(self):
    return "Just some hot water in a cup."

class Chocolate(HotBeverages):
  def __init__(self):
    super().__init__(price = 0.50, name = "chocolate")

  def description(self):
    return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverages):
  def __init__(self):
    super().__init__(price = 0.45, name = "cappuccino")

  def description(self):
    return "Un po' di Italia nella sua tazza!"
