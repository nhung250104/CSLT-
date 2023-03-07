toan=int(input())
ly=int(input())
hoa=int(input())
diemtrungbinh=((toan*2)+(ly*3)+hoa)/6
if diemtrungbinh<3:
    print("Kém")
elif diemtrungbinh<5:
    print("Yếu")
elif diemtrungbinh<6:
    print("Trung binh")
elif diemtrungbinh<7:
    print("Trung bình khá")
elif diemtrungbinh<8:
    print("Khá")
elif diemtrungbinh<9:
    print("Gioi")
else:
    print("Xuất sắc")
    
    
