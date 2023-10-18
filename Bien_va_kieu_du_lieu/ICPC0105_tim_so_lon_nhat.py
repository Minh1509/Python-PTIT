# Hàm để tìm số lớn nhất trong một xâu ký tự
def find_max_number(s):
    numbers = []
    num = ""
    for char in s:
        if char.isdigit():
            num += char
        elif num:
            numbers.append(int(num))
            num = ""
    if num:
        numbers.append(int(num))
    if numbers:
        return max(numbers)
    return None

# Đọc số lượng bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    test_string = input()
    result = find_max_number(test_string)
    if result is not None:
        print(result)