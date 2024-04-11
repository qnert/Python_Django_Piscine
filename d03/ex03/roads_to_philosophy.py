import requests, sys
from bs4 import BeautifulSoup

def main(search: str):
  url = "https://de.wikipedia.org/wiki/"
  request = requests.get(url + search)
  if request.status_code != 200:
    print("Error: couldn't get information from wikipedia.")
    return 1
  start_pos = int(str(request._content).find("<title>") + len("<title>"))
  end_pos = str(request._content).find(" ", start_pos)
  title = str(request._content)[start_pos:end_pos]
  print(title)




if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Error: wrong amount of arguments.")
  else:
    main(sys.argv[1])
