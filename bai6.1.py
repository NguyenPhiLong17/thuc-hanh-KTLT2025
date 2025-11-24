print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("##########################")
##################################




class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def dientich(self):
        return self.dai * self.rong


hcn = Hinhchunhat(5, 3)
print("Diện tích hình chữ nhật là:", hcn.dientich())

