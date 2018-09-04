
# 1
# 11
# 111
# 1111
# 11111

for num in range(1, 6):
    print("1" * num)

# 10000
# 11000
# 11100
# 11110
# 11111

for num in range(1, 6):
    print("1" * num + "0" * (5-num))

# 00100
# 01110
# 11111
# 01110
# 00100

for num in range(1, 6):
    num = 3 - num
    if num < 0:
        num = -num

    print("0" * num + "1" * (5 - 2 * num) + "0" * num)
