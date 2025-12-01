print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("##########################")
##################################

S = input("Nhập chuỗi S: ")

for ch in S:
    if ch not in [" ", "\t"]:     # nếu không phải space hoặc tab
        print(ch)
