# Program to read numbers from file and find total, max and min

try:
    with open("test.txt", "r") as file:
        numbers = file.read().split()
        numbers = [float(num) for num in numbers]

        total = sum(numbers)
        maximum = max(numbers)
        minimum = min(numbers)

        print("Total:", total)
        print("Maximum:", maximum)
        print("Minimum:", minimum)

except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("File contains non-numeric data!")
