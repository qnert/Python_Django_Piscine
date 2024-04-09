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

def check_and_print_input(input_str: str):
  result = display_city(input_str)
  if result != "":
    print(result)
    return 0
  result = display_state(input_str)
  if result != "":
    print(result)
    return (0)
  else:
    print(f"{input_str} is neither a capital city nor a state")

def input_check(input_str: str) -> list:
  x = input_str.find(',,')
  if (x != -1):
    sys.exit(1)
  lst = input_str.split(',')
  i = 0
  for item in lst:
    lst[i] = item.strip()
    i += 1
  i = 0
  for item in lst:
    lst[i] = item.title()
    i += 1
  return lst

def main(input_str: str):
  input_lst = input_check(input_str)
  for item in input_lst:
    if item != "":
      check_and_print_input(item)

if __name__ == "__main__":
  if len(sys.argv) > 2:
    print("Too many arguments!")
  elif len(sys.argv) == 1:
    print("Please provide a argument!")
  else:
    main(sys.argv[1])
