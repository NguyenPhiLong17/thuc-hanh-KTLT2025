print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("###########################")
###################################



import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius



r = float(input("Nhập bán kính hình tròn: "))
circle = Circle(r)

print("Diện tích:", circle.area())
print("Chu vi:", circle.circumference())
