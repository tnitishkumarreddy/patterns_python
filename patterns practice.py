'''n=int(input())

stars=0
for row in range(1,n+1):
    for st in range(0,stars+1):
        print(st,end=' ')
    print()
    stars+=1


n=int(input())
stars=n
for row in range(1,n+1):
    for st in range(0,stars+1):
        print(st,end=' ')
    print()
    stars-=1

n=int(input())

stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(stars,end=' ')
    print()
    stars+=1

n=int(input())

stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(st,end=' ')
    print()
    stars+=1

    
n=int(input())
s=n
stars=1
for row in range(1,n+1):
    for st in range(1,s+1):
        print(stars,end=' ')
    print()
    stars+=1
    s-=1


n=int(input())
s=n

stars=5
for row in range(1,n+1):
    for st in range(0,s):
        print(stars,end=' ')
    print()
    s-=1

n=int(input())
s=n

stars=0
for row in range(1,n+1):
    for st in range(0,s+1):
        print(st,end=' ')
    print()
    s-=1


n=int(input())
c=1

stars=1
for row in range(1,n+1):
    for st in range(1,c+1):
        print(stars,end=' ')
    print()
    stars+=2
    c+=1


n=int(input())
c=5

stars=5
for row in range(1,n+1):
    for st in range(1,c+1):
        print(stars,end=' ')
    print()
    stars-=1
    c-=1


n=int(input())
stars=1
for row in range(1,n+1):
    for st in range(stars,0,-1):
        print(st,end=' ')
    print()
    stars+=1


n=int(input())
stars=5
for row in range(1,n+1):
    for st in range(stars,0,-1):
        print(st,end=' ')
    print()
    stars-=1


n=int(input())
stars=1
c=1
for row in range(1,n+1):
    for st in range(stars,c-1,-1):
        print(st,end=' ')
    print()
    c+=row
    stars+=row+1

'''
n=int(input())
spaces=4
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(st,end=' ')
    print()
    spaces-=1
    stars+=1

