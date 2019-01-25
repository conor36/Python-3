import sys, string , operator
lines=sys.stdin.readlines()
p=lines[0].split()
ind=lines[1].split()
index=list(zip(p,ind))

scores={
-7:9,
-6:8,
-5:7,
-4:6,
-3:5,
-2:4,
-1:3,
0:2,
1:1,
2:0
    
}
a=[]
b={}
c={}

player=lines[2:]
for l in player:
   di=[]
   l=l.split()
   l[0]=" ".join(l[:-19])
   di.append(l[0])
   di=di+l[-19:]
   q=di[1]
   t=0
   j=2
   score=0
   for hole in index:
     free=0
     handicap= int(q)//18
     handicap1=int(q)%18
     if int(hole[1])<=handicap1:
      free=1+int(q)//18
     else:
      free=int(q)//18
   
     strokes=(di[j])
     if strokes not in string.ascii_letters and strokes not in string.punctuation:
      t=int(strokes)- free - int(hole[0])
      if t not in scores:
       scores[t]=0
      score=score+scores[t]
      j=j+1
     elif strokes=="X":
       j=j+1
     else: 
       t="Disqualified"
       score=t
   if score=="Disqualified":
    w=(l[0],score)
    a.append(w)

   else:
    c[l[0]]=score
data=c
c=sorted(c.items(),key=operator.itemgetter(-1),reverse=True)
for (k,v) in a:
 data[k]=v

max1=max(data.keys(),key=len)
max1=len(max1)

for x in a:
  c.append(x)

for y in c:
 print ('{:>{}s} : {:>2}'.format(y[0],max1,y[1])              )