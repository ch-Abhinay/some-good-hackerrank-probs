x,y=map(int,input().split())
vals=list(map(int,input().split()))
sol=[]
for a in range(1,len(vals)):
    if vals.index(a)+1>=y:
        i=vals.index(a)//y
        temp=vals[(y*i):]
        j=temp.index(a)
    else:
        i=0
        j=vals.index(a)
    if vals.index(a+1)>=y and a+1<len(vals)+1:
        k=vals.index(a+1)//y
        temp=vals[(y*k):]
        l=temp.index(a+1)
    else:
        k=0
        l=vals.index(a+1)
    if i+2==k and j+1==l or j-1==l:
        sol.append(True)
    elif i-2==k and j+1==l or j-1==l:
        sol.append(True)
    elif j+2==l and i+1==k or i-1==k:
        sol.append(True)
    elif j-2==l and i+1==k or i-1==k:
        sol.append(True)
    else:
        sol.append(False)
answer=True
for i in sol:
    if i==False:
        answer=False
print(answer)