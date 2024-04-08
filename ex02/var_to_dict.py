def create_dict() -> dict:
  d = [
    ('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammet' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante' , '1970'),
    ('Thompson' , '1949'),
    ('Burton' , '1939')
  ]

  dict = {}

  for i in d:
    if i[1] in dict.keys():
      dict[i[1]] = dict[i[1]] + " " + i[0]
    else:
      dict[i[1]] = i[0]
  return (dict)

def print_dict_format(dict):
  for i in dict:
    print(f"{i} : {dict[i]}")

if __name__ == "__main__":
  print_dict_format(create_dict())

