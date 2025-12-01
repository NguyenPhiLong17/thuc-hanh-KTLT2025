print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 2457520212610163")
print("##########################")
##################################


n = int(input("Nhập n: "))

fib = [0, 1]
while fib[-1] + fib[-2] < n:
    fib.append(fib[-1] + fib[-2])

print("Dãy Fibonacci:", fib)
