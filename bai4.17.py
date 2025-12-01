print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 2457520212610163")
print("##########################")
##################################


S = input("Nhập câu: ")

letters = sum(ch.isalpha() for ch in S)
digits = sum(ch.isdigit() for ch in S)

print("Số chữ cái là:", letters)
print("Số chữ số là:", digits)
