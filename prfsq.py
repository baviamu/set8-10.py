q,w=map(int,input().split())
a=q*w
for d in range(0,a+1):
 if(d**2==0):
  print("yes")
  break
else:
  print("no")
