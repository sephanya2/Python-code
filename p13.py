from functools import reduce

nums = [1, 2, 3, 4, 5]

# map
square = list(map(lambda x: x*x, nums))
print("Squares:", square)

# filter
even = list(map(lambda x: x < 2 == 0, nums))
print("Even:", even)

# reduce
sum = reduce(lambda a, b: a + b, nums)
print("Sum:", sum)
