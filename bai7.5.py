print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("###########################")
###################################



filename = input("Nhập tên tệp văn bản: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().split()

    max_len = max(len(word) for word in text)
    longest_words = [word for word in text if len(word) == max_len]

    print("Từ dài nhất:", longest_words)
    print("Độ dài:", max_len)

except FileNotFoundError:
    print(" Không tìm thấy tệp!")
