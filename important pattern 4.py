s=input()
ns=''
ns+=s[len(s)//2::]+s[:len(s)//2]
stars=1
spaces=6
for r in range(1,len(ns)+1):
    for sp in range(1,spaces+1):
        print(' ',end='')

    for st in range(stars):
        print(ns[st:st+1],end='')
    print()
    spaces-=1
    stars+=1
