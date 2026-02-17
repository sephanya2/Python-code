# User Defined Exception Example

class NegativeNumberError(Exception):
    pass
try:
    num = int(input("enter a positive number:"))
    print("your Number ",num)
    if num < 0:
            raise NegativeNumberError("negative number is not allowed")
except NegativeNumberError as e:
    print("custom exception:",e)
except ValueError:
    print("Please enter a valid integer.")    
    




