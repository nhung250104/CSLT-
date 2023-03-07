niemyet=float(input("Nhap Gia niem yet="))
chietkhau=float(input("Nhap Chiet khau="))

VAT=(niemyet-chietkhau)*0.01
ban=niemyet-chietkhau+VAT

print("Giaban:",ban)