print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("###########################")
###################################



filename = input("Nhập tên tệp cần đếm dòng: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        count = sum(1 for line in file)
        print("Số dòng trong tệp là:", count)
except FileNotFoundError:
    print(" Không tìm thấy tệp!")
