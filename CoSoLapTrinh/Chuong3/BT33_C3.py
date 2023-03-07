tieuthu=int(input("tieu thu="))
gia1=550
gia2=750
gia3=950
gia4=1350

if tieuthu<=100:
    tiendien=tieuthu*gia1
elif tieuthu<=150:
    tiendien=100*gia1 + (tieuthu-100)*gia2
elif tieuthu<=200:
    tiendien=100*gia1 + 50*gia2 + (tieuthu-150)*gia3
else:
    tiendien=100*gia1 + 50*gia2 + 50*gia3 + (tieuthu-200)*gia4
    
phaitra=tiendien*1.1
print("phaitra=",phaitra,sep="")
