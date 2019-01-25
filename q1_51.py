import sys

def main():
  s=list(sys.argv[1])
  i=0
  j=1

  if len(s)%2==0:
    while j<=len(s):
      tmp=s[i]
      s[i]=s[j]
      s[j]=tmp
      i+=2
      j+=2
  else:
    while j<len(s)-1:
      tmp=s[i]
      s[i]=s[j]
      s[j]=tmp
      i+=2
      j+=2

  print("".join(s))

if __name__ == '__main__':
    main()


