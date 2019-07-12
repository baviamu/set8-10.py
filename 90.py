bc=input()
f=[]
for o in bc:
	if o.isnumeric():
		f.append(o)
print(''.join(f))
