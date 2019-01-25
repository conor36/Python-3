import sys

def evil(l):
    t = ["e", "v", "i", "l"]
    w = ""
    for c in l.lower():
       if c in t:
          w += c
    if w == "evil":
       print (l.strip("\n"))
    


def main():
   for line in sys.stdin:
      evil(line)

if __name__ == "__main__":
   main()
