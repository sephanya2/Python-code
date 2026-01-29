#largest Odd Number 


largest_odd = None

print("Enter 10 numbers:")
for i in range(10):
    num = int(input())

    if num % 2 != 0:
        if largest_odd is None or num > largest_odd:
            largest_odd = num

if largest_odd is not None:
    print("Largest odd number:", largest_odd)
else:
    print("No odd number found")
