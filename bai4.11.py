print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 2457520212610163")
print("##########################")
##################################


n = int(input("Nhập n: "))

def sum_divisors(x):
    return sum(i for i in range(1, x) if x % i == 0)

for num in range(1, n):
    if sum_divisors(num) > num:
        print(num)
