import sys
lines = sys.stdin.readlines()

for line in lines:
   line = line.casefold().split()
   output = ""
   for word in line:
      if not word.isalnum():
         word = word[:-1]
      output += word
   if output == output[::-1]:
      print(True)
   else:
      print(False)

