import sys
a = sys.stdin.readlines()

for noun in a:
   noun = noun.strip()
   if (noun.endswith("ch") or noun.endswith("sh") or noun.endswith("z") or noun.endswith("x") or noun.endswith("s")) == True:
      plural = noun + "es"
   elif noun.endswith("y") == True and (noun.endswith("ay") or noun.endswith("ey") or noun.endswith("iy") or noun.endswith("oy") or noun.endswith("uy")) == False:
      plural = noun[:-1] + "ies"
   elif noun.endswith("f") == True:
      plural = noun[:-1] + "ves"
   elif noun.endswith("fe") == True:
      plural = noun[:-2] + "ves"
   elif noun.endswith("o") == True:
      plural = noun + "es"
   else:
      plural = noun + "s"
   print(plural)
  
