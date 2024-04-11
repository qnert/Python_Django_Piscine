import dewiki, requests, json, sys

def main(search: str):
  url = "https://en.wikipedia.org/w/api.php"
  params = {
    "action": "query",
    "titles": search,
    "prop": "extracts",
    "format": "json",
    "explaintext": True
  }
  request = requests.get(url, params)
  if request.status_code != 200:
    print("Error: couldn't get information from api.")
    return 1
  data = request.json()
  id = next(iter(data["query"]["pages"]))
  try:
    page_content = data["query"]["pages"][id]["extract"]
  except:
    print("Error: searched site was no found.")
    return 1
  with open(search + ".wiki", "w") as f:
    f.write(page_content)
    f.close()

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Error: wrong amount of arguments.")
  else:
    main(sys.argv[1])
