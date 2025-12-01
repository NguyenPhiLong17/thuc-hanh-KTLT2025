print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 2457520212610163")
print("##########################")
##################################

S = input("Nhập câu: ")

upper = sum(ch.isupper() for ch in S)
lower = sum(ch.islower() for ch in S)

print("Chữ hoa:", upper)
print("Chữ thường:", lower)
