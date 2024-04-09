import os, re, sys
from settings import *

def main(input: str):
  try:
    if not input.endswith(".template"):
       print("Wrong file ending!")
       return 1
    with open(input, 'r') as f:
        content = f.read()
        f.close()
    content = content.replace("{name}", name)
    content = content.replace("{link}", link)
    with open("CV.html", 'w') as f:
       f.write(content)
       f.close()
  except FileNotFoundError:
      print("File not found.")
  except PermissionError:
      print("Permission denied.")
  except IsADirectoryError:
      print("Is a directory.")
  except NameError:
      print("Check settings.py for name and link variable!")

if __name__ == "__main__":
  if len(sys.argv) > 2:
    print("Too many argmuents!")
  elif len(sys.argv) == 1:
    print("Please provide a template file!")
  else:
    main(sys.argv[1])
