print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("###########################")
###################################



# Nhập tên file từ người dùng
filename = input("Nhập tên tệp cần đọc: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print("Nội dung tệp:")
        print(content)
except FileNotFoundError:
    print(" Không tìm thấy tệp!")
