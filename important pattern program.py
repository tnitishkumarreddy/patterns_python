n=int(input())
d=1
for r in range(1,n+1):
    for st in range(1,n+1):
        if r%2==1:
            print(d,end=' ')
            d+=1
        else:
            
            print(d,end=' ')
            d-=1
    print()
    if r%2==0:
        d=(n*r)+1
    else:
        d+=4
