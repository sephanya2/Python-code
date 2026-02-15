# Basic Exception Handling 

num1 = int (input("enter first number:"))
num2 = int(input("enter the second number:"))
try:
  result = num1/num2
  print("result:",result)
except ZeroDivisionError:
    print("error:cannot divide by zero!") 
