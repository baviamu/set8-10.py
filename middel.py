sttg=list(input())
if len(sttg)%2==0:
    sttg[int(len(sttg)/2)] ='*'
    sttg[int(len(sttg)/2)-1]='*'
else:
    sttg[int(len(sttg)/2)] ='*'
for m in range(0,len(sttg)):
    print(sttg[m],end='')
