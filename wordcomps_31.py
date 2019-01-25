import sys
words = [word.strip() for word in sys.stdin.read().split()]

print ("Words containing 17 letters: {}".format([word for word in words if len(word) == 17]))
print("Words containing 18+ letters: {}".format([word for word in words if len(word) >= 18]))
print("Shortest word containing all vowels: {}".format(sorted([word for word in words if set('aeiou').issubset(word.lower())], key=len) [0]))
print("Words with 4 a's: {}".format([word for word in words if word.lower().count('a') == 4]))
print("Words with 2+ q's: {}".format([word for word in words if word.lower().count('q') == 2]))
print("Words containing cie: {}".format([word for word in words if 'cie' in word])) 
print("Anagrams of angle: {}".format([word for word in words if word != "angle" and len(word) == len('angle') and set('angle').issubset(word.lower())]))
print("Words ending in iary: {}".format(len([word for word in words if word.endswith('iary')])))
print("Words with q but no u: {}".format([word for word in words if word.lower().count('q') > 0 and word.lower().count('qu') == 0 ]))

e_max = [word for word in sorted(words, key=lambda word: word.count('e'), reverse=True)][0].count('e')

print("Words with most e's: {}".format([word for word in words if word.count('e') == e_max]))


