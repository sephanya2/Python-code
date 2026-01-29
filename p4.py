#armstrong number

numbers = []
print("Enter 10 numbers:")
for i in range(10):
    numbers.append(int(input()))

print("Armstrong Numbers:")
for num in numbers:
    temp = num
    sum = 0
    while temp > 0:
        d = temp % 10
        sum += d ** 3
        temp //= 10
    if sum == num:
        print(num)
