import sys
import antigravity as ag

def main(argv):
  try:
    latitude = float(sys.argv[1])
  except Exception as e:
    print(e)
  try:
    longitude = float(sys.argv[2])
  except Exception as e:
    print(e)
  try:
    datedow = sys.argv[3].encode('utf-8')
  except Exception as e:
    print(e)
  ag.geohash(latitude, longitude, datedow)

if __name__ == "__main__":
  if len(sys.argv) == 4:
    main(sys.argv)
  else:
    print("Error: wrong amout of arguments.")
