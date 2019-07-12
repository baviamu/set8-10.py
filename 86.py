av=list(input())
ni=[]
for g in av:
   if g not in ni:
      ni.append(g)
if av==ni:
   print("Yes")
else:
   print("No")
