b1,b2=map(int,input().split())
char=input().split()
f=[]
for y in char:
	if(int(y)%2!=0):
		f.append(y)
print(f[b2-1])
