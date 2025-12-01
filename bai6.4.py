print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("###########################")
###################################



class StringHandle:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.s.upper())


# Sử dụng class
str_obj = StringHandle()
str_obj.get_String()
str_obj.print_String()
