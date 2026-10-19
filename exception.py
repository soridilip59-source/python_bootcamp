try:
    num1= float(input("Enter first number: "))
    num2= float(input("Enter first number: "))

    result = num1/num2

    print("Result: ",result)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Error You can't divide by zero.")
finally:
    print("Calculate program finished.")
