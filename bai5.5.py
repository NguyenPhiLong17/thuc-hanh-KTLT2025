print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("##########################")
##################################



import numpy as np

# Dữ liệu đầu vào
data = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]

# Khai báo kiểu dữ liệu có cấu trúc
dtype = [('name', 'U10'), ('class', 'i4'), ('height', 'f4')]

# Tạo mảng
students = np.array(data, dtype=dtype)

# Sắp xếp theo class, rồi theo height
sorted_students = np.sort(students, order=['class', 'height'])

print(sorted_students)
