import sys
line=sys.stdin.readline()
while line:
    line=line.strip() 
    Total=0
    isdigit=0
    islower=0
    isupper=0
    special=0
    
    for c in line:


        if c.isdigit():
           isdigit=1

        elif c.isupper():
           isupper=1

        elif c.islower():
           islower=1

        else:
           special=1

    Total=isdigit+islower+special+isupper
    print(Total)
    line=sys.stdin.readline()

