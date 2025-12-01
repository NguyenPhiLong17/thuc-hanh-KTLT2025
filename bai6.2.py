print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("###########################")
###################################


class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        words = self.text.split()     
        words.reverse()              
        return " ".join(words)        


# Ví dụ sử dụng:
inp = "hello .py"
rev = ReverseWords(inp)
print("Kết quả:", rev.reverse())
