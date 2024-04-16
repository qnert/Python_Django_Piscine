import requests, sys
from bs4 import BeautifulSoup

def wiki_crawl(search: str, history: set) -> int:
  url = "https://en.wikipedia.org" + search
  request = requests.get(url)
  if request.status_code != 200:
    print("It leads to a dead end! So it took 0", end = '')
    return
  soup = BeautifulSoup(request.content, 'html.parser')
  title = soup.select_one("#firstHeading").text
  print(title)
  if title != "Philosophy":
    content = soup.find(id='mw-content-text')
    links = content.select('p > a')
    for link in links:
      if link.get('href') in history:
        print('It leads to an infinite loop! So it took 0', end = '')
        return
      elif link.get('href') is not None and link['href'].startswith('/wiki/')\
            and all(c != ':' for c in link['href']):
        history.add(search)
        wiki_crawl(link['href'], history)
        return
      else:
        return
  else:
    print("It took " + str(len(history)), end = '')
    return
  print("It couldn't be resolved within any amount of", end = '')

def main(search: str):
  wiki_crawl("/wiki/" + search, set())
  print(" tries to get from " + search + " to Philosophy")


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Error: wrong amount of arguments.")
  else:
    main(sys.argv[1])

