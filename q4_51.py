
import sys
import math

def mean(l):
   total = (sum(l))
   avg = total / len(l)
   print ("Mean: {:.1f}".format(avg))

def mode_num(l):
   mode = 0 
   for num in l:
      if l.count(num) > mode:
         mode = int(num)
   print ("Mode: {:.1f}".format(mode))

def median(l):
   l = sorted(l)

   n = len(l)

   if n % 2 == 0:
      ans = (l[int(n/2)] + l[int((n/2-1))])/2
      print ("Median: {:.1f}".format(ans))
   else:
      ans2 = l[int(n/2)]
      print ("Median: {:.1f}".format(ans2))

def main():
   l = []
   for line in sys.stdin:
      l.append(int(line))

   mean(l)
   mode_num(l)
   median(l)

if __name__ == "__main__":
    main()
