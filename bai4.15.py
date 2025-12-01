print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 2457520212610163")
print("##########################")
##################################

S = input("Nhập chuỗi nhị phân: ")
lst = S.split(",")

result = []
for x in lst:
    if int(x, 2) % 5 == 0:
        result.append(x)

print(",".join(result))
