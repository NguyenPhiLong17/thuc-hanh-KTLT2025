lst = list(map(int, input("Nhập các số cách nhau bằng dấu phẩy: ").split(',')))
le = [x for x in lst if x % 2 == 1]
print(",".join(map(str, le)))
