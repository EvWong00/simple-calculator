import math
#creating a menu for the user

print("Select an operation to perform: (1 to 6)")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square Root")
print("6.Raise to Power")

operation = input()

if operation == "1": #addition
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))

elif operation == "2": #subtraction
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is " + str(int(num1) - int(num2)))

elif operation == "3": #multiplication
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is " + str(int(num1) * int(num2)))

elif operation == "4": #division
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The result is " + str(int(num1) / int(num2)))

elif operation == "5": #square root
    num = int(input("Enter number: "))
    
    print("The square root is %f " %(math.sqrt(num)))

elif operation == "6": #square a number
    num = int(input("Enter number: "))
    
    print("The power is %d " %(pow(num, 2)))

else:
    print("Invalid Entry")