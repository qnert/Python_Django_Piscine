import sys

def display_city(state: str):
  states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
  capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
  if state in states.keys():
    print(f"{capital_cities[states[state]]}")
  else:
    print("Unknown state.")

if __name__ == "__main__":
  if len(sys.argv) > 2:
    print("Too many arguments!")
  elif len(sys.argv) == 1:
    print("Please provide a argument!")
  else:
    display_city(sys.argv[1])
