# Vòng lặp For
# In ra 10 số tự nhiên đầu tiên từ 1 đến 10
for i in range(1, 11):
    print(i)

# Tính tổng các số tự nhiên từ 1 đến n
n = int(input("Nhập vào số nguyên dương n: "))
sum_numbers = 0
for i in range(1, n + 1):
    sum_numbers += i
print("Tổng các số từ 1 đến n là:", sum_numbers)

# In ra bảng cửu chương của n từ 1 đến 10
n = int(input("Nhập vào số nguyên dương n: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Đếm số chữ số của n
n = int(input("Nhập vào số nguyên dương n: "))
print("Số chữ số của n là:", len(str(n)))

# Tính tổng các chữ số của n
n = int(input("Nhập vào số nguyên dương n: "))
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n //= 10
print("Tổng các chữ số của n là:", sum_digits)

# In ra tam giác với số tăng dần theo từng dòng
n = int(input("Nhập vào số nguyên dương n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# In ra tam giác với số giảm dần theo từng dòng
n = int(input("Nhập vào số nguyên dương n: "))
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# Tính giai thừa của n
n = int(input("Nhập vào số nguyên dương n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Giai thừa của {n} là {factorial}")

# In ra số đảo ngược của n
n = int(input("Nhập vào số nguyên dương n: "))
print("Số đảo ngược của n là:", int(str(n)[::-1]))

# In ra tam giác với mỗi dòng là số n lặp lại tăng dần theo số dòng
n = int(input("Nhập vào số n (từ 1 đến 9): "))
for i in range(1, n + 1):
    print(str(i) * i)

# Tách từng từ trong câu và in ra cùng với độ dài của từ đó
sentence = input("Nhập vào một câu: ")
words = sentence.split()
for word in words:
    print(f"{word} {len(word)}")

# Tính tổng của hai số nguyên được nhập vào và cách nhau bởi dấu phẩy
input_string = input("Nhập vào hai số nguyên cách nhau bởi dấu phẩy: ")
numbers = input_string.split(',')
sum_two_numbers = int(numbers[0]) + int(numbers[1])
print("Tổng của hai số là:", sum_two_numbers)

# Đếm số chữ số chẵn trong một chuỗi
s = input("Nhập vào một chuỗi: ")
count_even_digits = 0
for char in s:
    if char.isdigit() and int(char) % 2 == 0:
        count_even_digits += 1
print("Số chữ số chẵn trong chuỗi là:", count_even_digits)

# Tìm tất cả các phương án để có tổng 200.000đ từ 3 loại giấy bạc
total_amount = 200000
for i in range(total_amount // 1000 + 1):
    for j in range(total_amount // 2000 + 1):
        for k in range(total_amount // 5000 + 1):
            if 1000 * i + 2000 * j + 5000 * k == total_amount:
                print(f"1000 VND: {i}, 2000 VND: {j}, 5000 VND: {k}")

# Kiểm tra chuỗi ngoặc có hợp lệ không
s = input("Nhập vào chuỗi ngoặc: ")
stack = []
pairs = {'(': ')', '[': ']', '{': '}'}
valid = True
for char in s:
    if char in pairs:
        stack.append(char)
    elif stack and char == pairs[stack[-1]]:
        stack.pop()
    else:
        valid = False
        break
print("Chuỗi ngoặc hợp lệ:", valid and not stack)

# Chuyển đổi từ số La Mã sang số nguyên
s = input("Nhập vào một chuỗi số La Mã: ")
roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
integer_value = 0
for i in range(len(s)):
    if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
        integer_value -= roman_to_int[s[i]]
    else:
        integer_value += roman_to_int[s[i]]
print("Giá trị số nguyên là:", integer_value)

# Vẽ xe lửa với kích thước chỉ định
size = int(input("Kích thước của xe lửa là bao nhiêu? "))
for i in range(size):
    if i < size - 1:
        print(" _________________________", end="   ")
    else:
        print(" ______________________>__\n")
    if i < size - 1:
        print("|]||[]_[]_[]|||[]_[]_[]||[|", end=" |")
    else:
        print("|]||[]_[]_[]|||[]_[]_[]||[|\n")
    if i < size - 1:
        print("\\==o-o======o-o======o-o==/", end="/\\")
    else:
        print("\\==o-o======o-o======o-o==/\n")

# Vòng lặp While
# Khởi động 1: In ra tất cả các số chia hết cho cả 5 và 7 trong khoảng từ 1500 đến 2700
i = 1500
while i <= 2700:
    if i % 5 == 0 and i % 7 == 0:
        print(i)
    i += 1

# Bài 1: In tam giác vuông giảm dần từ chiều cao nhập vào
height = int(input("Nhập chiều cao của tam giác: "))
while height > 0:
    print('*' * height)
    height -= 1

# Bài 2: In tam giác vuông với dấu cách giữa các '*'
height = int(input("Nhập chiều cao của tam giác: "))
while height > 0:
    print('* ' * height)
    height -= 1

# Bài 3: In tam giác vuông xen kẽ * và -
# Cách 1:
height = int(input("Nhập chiều cao của tam giác: "))
while height > 0:
    line = ''
    for j in range(height):
        if j % 2 == 0:
            line += '*'
        else:
            line += '-'
    print(line)
    height -= 1
# Cách 2: 
height = int(input("Please input height: "))

i = height

while i >= 1:
    print (('* - ' * (i // 2) + '*' * (i % 2)).strip())
    i -= 1

# Bài 4: In các số từ 1 đến n với các quy tắc đặc biệt
n = int(input("Nhập vào số nguyên n: "))
i = 1
while i <= n:
    if i % 3 == 0 and i % 4 == 0:
        print("python")
    elif i % 3 == 0:
        print("py")
    elif i % 7 == 0:
        print("thon")
    else:
        print(i)
    i += 1

# Bài 5: Kiểm tra số nguyên tố
num = int(input("Nhập một số để kiểm tra số nguyên tố: "))
if num > 1:
    i = 2
    is_prime = True
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, "là số nguyên tố")
    else:
        print(num, "không phải là số nguyên tố")

# Bài 6: Trò chơi kéo búa bao
import random

while True:
    player_choice = int(input("Mời lựa chọn(1 - búa, 2 - kéo, 3 - bao): "))
    computer_choice = random.randint(1, 3)
    if (player_choice == 1 and computer_choice == 2) or \
       (player_choice == 2 and computer_choice == 3) or \
       (player_choice == 3 and computer_choice == 1):
        print(f"Máy tính chọn: {computer_choice}\nNgười chơi thắng.")
        break
    else:
        print(f"Máy tính chọn: {computer_choice}\nNgười chơi thua.")
