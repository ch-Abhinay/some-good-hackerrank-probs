def print_rangoli(size):
    alpha='abcdefghijklmnopqrstuvwxyz'
    num=len(alpha[size:0:-1]+alpha[1:size])*2-1
    # print(num)
    n=1
    a=size-1
    r=[]
    while n<=size:
        val=alpha[size-1:a:-1]+alpha[a:size]
        ans=''
        for g in val:
            ans+=g+'-'
        r.append(ans[:len(ans)-1])
        n+=1
        a=a-1
    for i in range(len(r)):
        print(r[i].center(num,'-'))
    r.reverse()
    for i in range(1,len(r)):
        print(r[i].center(num,'-'))

n = int(input())
print_rangoli(n)