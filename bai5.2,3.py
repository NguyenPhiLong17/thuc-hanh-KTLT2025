print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("##########################")
##################################


from my_module import tim_lon_nhat

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

# Nhập danh sách
lst = []
for i in range(n):
    val = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(val)

# Tìm phần tử lớn nhất và nhỏ nhất
max_value = tim_lon_nhat(lst)
min_value = min(lst)

# Tìm vị trí
max_index = lst.index(max_value)
min_index = lst.index(min_value)

print("Danh sách đã nhập:", lst)
print("Phần tử lớn nhất:", max_value, "tại vị trí", max_index)
print("Phần tử nhỏ nhất:", min_value, "tại vị trí", min_index)
