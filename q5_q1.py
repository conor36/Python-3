import sys

def seconds(t):
   [mins, secs] = t.split(":")
   totals = int(mins)*60 + int(secs)
   return totals

def sorter(t):
   return seconds(t[-1])


def main():
   d = {}
   for line in sys.stdin:
      try:
         details = line.split()
         d[details[0]] = min(details[1:], key = seconds)
      except ValueError:
         continue

   winner = min(d.items(), key=sorter)
   print ("{} : {}".format(winner[0], winner[1]))

if __name__ == "__main__":
main()
