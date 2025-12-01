print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("##########################")
##################################

import math

def Tinh(R):
    if R <= 0:
        print("Ban kinh khong hop le!")
        return
    
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R
    
    print("Chu vi hinh tron =", chu_vi)
    print("Dien tich hinh tron =", dien_tich)

# Gọi hàm sau khi nhập bán kính
R = float(input("Nhap ban kinh R: "))
Tinh(R)
