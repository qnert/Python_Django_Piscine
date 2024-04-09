import sys

def display_state(city: str):
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
  key_city = [key for key, value in capital_cities.items() if value == city]
  if key_city:
    key_state = [key for key, value in states.items() if value == key_city[0]]
    if key_state:
      print(key_state[0])
  else:
    print("Unknown capital city.")

if __name__ == "__main__":
  if len(sys.argv) > 2:
    print("Too many arguments!")
  elif len(sys.argv) == 1:
    print("Please provide a argument!")
  else:
    display_state(sys.argv[1])
