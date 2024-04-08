import sys

def display_state(city: str) -> str:
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
      return(f"{city} is the capital of {key_state[0]}")
  else:
    return("")

def display_city(state: str) -> str:
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
    return(f"{capital_cities[states[state]]} is the capital of {state}")
  else:
    return("")

def check_and_print_input(input: str):
  result = display_city(input)
  if result != "":
    print(result)
    sys.exit(0)
  result = display_state(input)
  if result != "":
    print(result)
    sys.exit(0)
  else:
    print(f"{input} is neither a capital city nor a state")

def main(input: str):
  check_and_print_input(str)

if __name__ == "__main__":
  if len(sys.argv) > 2:
    print("Too many arguments!")
  elif len(sys.argv) == 1:
    print("Please provide a argument!")
  else:
    main(sys.argv[1])
