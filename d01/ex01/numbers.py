
def get_file_from_str() -> str:
  with open("numbers.txt", "r") as nb_file:
    content = nb_file.read()
    nb_file.close()
  return (content)

def display_content(str):
  print(str.replace(",", "\n"))

def main():
  display_content(get_file_from_str())

if __name__ == "__main__":
  try:
    main()
  except AssertionError as e:
    print(e)
