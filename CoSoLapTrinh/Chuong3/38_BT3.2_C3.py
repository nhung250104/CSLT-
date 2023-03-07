n=int(input('Nhap n tu 1 - 50: '))
i=1
while i<=n:
    if i%10!=0:
        print(i,end=" ")
    elif i%10==0:
        print(i)
    i=i+1
