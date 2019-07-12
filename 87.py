ley,maz=map(int,input().split())
wos=[]
ed=[]
gcd=1
for t in range(1,ley+1):
    if(ley%t==0):
        wos.append(t)
for l in range(1,maz+1):
    if(maz%l==0):
        ed.append(l)
for h in wos:
    if h in ed:
        gcd=gcd*h
print(gcd)
