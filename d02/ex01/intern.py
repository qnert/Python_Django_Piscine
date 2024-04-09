class Intern:
  def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
    self.name = name

  class Coffee:
    def __str__(self):
      return "This is the worst coffee you ever tasted."

  def __str__(self):
    return f"{self.name}"

  def work(self):
    raise Exception("I'm just an intern. I can't do that...")

  def make_coffee(self):
    return self.Coffee()

def main():
  a = Intern()
  b = Intern("Mark")

  print(a)
  print(b)

  print(b.make_coffee())
  try:
    a.work()
  except Exception as e:
    print(e)

if __name__ == "__main__":
  main()
