print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("##########################")
##################################

S = input("Nhập chuỗi: ")

ket_qua = ""
for ch in S:
    if not ch.isdigit():    
        ket_qua += ch

print("Chuỗi sau khi loại bỏ chữ số:", ket_qua)
