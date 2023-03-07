M1=int(input("M1="))
M2=int(input("M2="))
M3=int(input("M3="))
tieuthu=int(input("S="))

if tieuthu<=100:
    print("Phai tra=",tieuthu*M1)
elif tieuthu<=150: 
    print("Phai tra=",100*M1 + (tieuthu-100)*M2 )
else:
    print("Phai tra=",100*M1 + 50*M2 + (tieuthu-150)*M3,sep="")
