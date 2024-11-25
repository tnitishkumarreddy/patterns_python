
n=6
stars=6
spaces=1
for r in range(1,n+1):
    d=r
    if r==1 or r==2:
        for sp in range(1,spaces+1):
            print(' ',end=' ')
        for st in range(1,stars+1):
            print(d,end=' ')
            d+=n+1-st

    else:
        for st in range(1,stars+1):
            print(d,end=' ')
            d+=n+1-st
    print()
    stars-=1
            

n=6
stars=6
spaces=1
for r in range(1,n+1):
    d=r
    for st in range(1,stars+1):
        print(d,end=' ')
        d+=n+1-st
    print()
    stars-=1
