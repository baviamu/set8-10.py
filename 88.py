f,g=map(int,input().split())
if(f>g):
  gt=f
else:
  gt=g
while(True):
  if((gt%f) == 0 and (gt%g) == 0):
    lcm=gt
    break
  gt=gt+1
print(lcm)
