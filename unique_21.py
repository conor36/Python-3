import sys
import string

lines = sys.stdin.read().split()

unique_words = []

exclude = set(string.punctuation + " " + "\n")

for word in lines:
   
   word = word.casefold()
   
   if not word.isalnum():
      word = ''.join(ch for ch in word if ch not in exclude)
   
   if word not in unique_words and word != "":
      unique_words.append(word)

print(len(unique_words))
