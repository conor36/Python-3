import sys

line = sys.stdin.readline()

while 0 < len(line):
	line = line.split()
	s = ""

	for word in line:
		last = word[-1]
		word = word[:-1] + last.capitalize()
		s += word + " "

	print(s.strip())
	
	line = sys.stdin.readline()	