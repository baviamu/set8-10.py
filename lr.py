des=int(input())
P,Q=list(map(int,input().split()))
for o in range(P+1,Q+1) :
    if (des==o) :
        print("yes")
        break
else :
    print("no")
