import sys 

line = sys.stdin.readline()

while 0 < len(line):
	line = line.split()
	
	print(" ".join(word.capitalize() for word in line))
	
	line = sys.stdin.readline()