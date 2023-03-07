i=1
j=1
t=1
l=1
while j<=9:
    if i//9 == j and i%9 == 0:
        g=l*t
        print(g)
        j=j+1
        t=t+1
        l=0
    elif j <= 9:    
         g=l*t
         print(g,end=" ")
    i=i+1
    l=l+1