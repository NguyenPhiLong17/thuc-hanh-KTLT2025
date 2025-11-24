print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("###########################")
###################################



filename = "output.txt"
data = ["Xin chào", "Python", "Ghi dữ liệu vào file", "Dòng cuối"]

with open(filename, "w", encoding="utf-8") as file:
    for item in data:
        file.write(item + "\n")

print("Đã ghi danh sách vào file", filename)
