print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("###########################")
###################################



source = input("Nhập tên tệp nguồn: ")
dest = input("Nhập tên tệp đích: ")

try:
    with open(source, "r", encoding="utf-8") as src:
        content = src.read()

    with open(dest, "w", encoding="utf-8") as dst:
        dst.write(content)

    print("Đã sao chép nội dung từ", source, "sang", dest)

except FileNotFoundError:
    print(" Tệp nguồn không tồn tại!")
