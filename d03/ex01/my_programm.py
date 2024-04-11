from local_lib import path

def main():
  try:
    path.Path.mkdir(path.Path() + "/tmp")
  except Exception as e:
    pass
  with open("./tmp/tmp_file.txt", "w") as f:
    f.write("42 Marocco is a school of cheaters!")
    f.close()
  with open("./tmp/tmp_file.txt", "r") as f:
    print(f.read())
    f.close()

if __name__ == "__main__":
  main()
