def divide_two_numbers(num1,num2):
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:
        return "error:cannot divide by zero"
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print(divide_two_numbers(num1,num2))