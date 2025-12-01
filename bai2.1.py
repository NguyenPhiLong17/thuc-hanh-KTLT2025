print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 2457520216101")
print("##########################")
##################################


import math

# Nhập hệ số
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Trường hợp a = 0 → phương trình bậc nhất
if a == 0:
    if b != 0:
        x = -c / b
        print("Phương trình bậc nhất, nghiệm x =", x)
    else:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
else:
    # Tính delta
    delta = b*b - 4*a*c

    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
