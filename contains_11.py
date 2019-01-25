import sys 

letter = sys.argv[1]
word = sys.argv[2]

len = len(letter)
count = 0 

for letter in letter:
  if letter in word:
    count += 1 
    word = word.replace(letter, '')

if count == len:
  print (True)

else:
  print (False)
