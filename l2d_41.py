import sys

d = {}
 
def l2d(f):
   lines = f.readlines()
   i = 0 
   while i < len(lines[0].split()):
      d[lines[0].split()[i]] = lines[1].split()[i]
      i = i + 1
   return (d)
