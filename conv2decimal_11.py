import sys 
base = sys.argv[2]
number = sys.argv[1]

dec = 0
i = 0
while i < len(number):
  power = len(number) - i - 1
  dec = dec + int(number[i]) * (int(base) ** power)
  i += 1 
print (dec)
