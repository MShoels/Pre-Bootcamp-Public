# 1 Basic
for i in range(1, 150, 1):
    print(i)

# 2 Multiples of 5
for i in range(5, 1000, 5):
    print(i)

# 3 Counting, The Dojo Way
for num in range(100):
    if num % 5 == 0:
        print("Coding")
    elif num % 10 == 0:
        print("Coding Dojo")
    else:
        print(num)

# 4 Whoa. That Sucker's Huge
final_sum = 0
for i in range(1, 500000, 2):
    final_sum += i
    print(final_sum)

# 5 Countdown by fours
for count in range(2018, 0, -4):
    print(count)

# 6 Flexible Counter
Low_Num, Mult, High_Num = 2, 3, 9
for Mult in range (3, 12, 3):
    print(Mult)