# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    s=sum(l)
    sumi=s
    for i in l:
        if i>b:
            sumi=sumi-(i-b)
    print(s-sumi)
