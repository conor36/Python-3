import sys 
import string
d = {}
s = [line.strip().lower() for line in sys.stdin.read().split()]
for a in s:
   a = "".join([char for char in a if char not in set("!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~")])
   if a in d:
       d[a] += 1
   else:
       d[a]  = 1

max1 = len(max([k for k in sorted(d) if len(k) > 3 and int(d[k]) >= 3], key = len))
max2 = len(str(max([d[n] for n in sorted(d) if len(n) > 3 and int(d[n]) >= 3])))

for key in sorted(d):
   if len(key) > 3 and d[key] >=3:
      print ("{:>{:d}s} : {:{:>d}}".format(key, max1, d[key],max2))
