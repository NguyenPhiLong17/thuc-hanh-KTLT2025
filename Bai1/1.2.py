n = int(input("Nhập số nguyên dương n: "))

if n == 1:
    print(n, "không là số nguyên tố")
else:
    if n < 4:
        print(n, "là số nguyên tố")
    else:
        i = 2  
        while i < n and n % i != 0:
            i += 1
        if i == n:
            print(n, "là số nguyên tố")
        else:
            print(n, "không là số nguyên tố")

