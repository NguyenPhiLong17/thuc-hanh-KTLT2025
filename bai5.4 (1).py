print("Sinh viên: Nguyễn Phi Long")
print("Mssv: 245752021610163")
print("##########################")
##################################



# sequential_search.py
def Sequential_Search(lst, item):
    """
    Tìm tuần tự item trong lst.
    Trả về (True, index) nếu tìm thấy (index là 0-based),
    hoặc (False, -1) nếu không tìm thấy.
    """
    i = 0
    n = len(lst)
    while i < n:
        if lst[i] == item:
            return True, i
        i += 1
    return False, -1

# Nếu chạy trực tiếp file này, chương trình sẽ hỏi đầu vào từ bàn phím
if __name__ == "__main__":
    try:
        n = int(input("Nhập số phần tử n: ").strip())
    except ValueError:
        print("Giá trị n không hợp lệ.")
        exit(1)

    print("Nhập các phần tử (cách nhau bởi dấu cách) hoặc nhập từng dòng:")
    elems = input().strip().split()
    # nếu người dùng nhập ít hơn n phần tử, tiếp tục đọc cho đủ
    while len(elems) < n:
        elems += input().strip().split()

    # Chuyển phần tử sang int nếu có thể (nếu là số)
    try:
        lst = [int(x) for x in elems[:n]]
    except ValueError:
        # nếu không phải số, giữ dưới dạng chuỗi
        lst = elems[:n]

    # Nhập item cần tìm (cố gắng chuyển thành int khi có thể)
    raw_item = input("Nhập phần tử cần tìm: ").strip()
    try:
        item = int(raw_item)
    except ValueError:
        item = raw_item

    found, idx = Sequential_Search(lst, item)
    if found:
        print("Kết quả: (True, {})".format(idx))
    else:
        print("Kết quả: (False, -1)")
