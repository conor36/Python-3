import sys 
a = sys.stdin.readlines()

i = 0

total = 0 

while i < len(a):
	total = total + int(a[i])
	i = i + 1
print total