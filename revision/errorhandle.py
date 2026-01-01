try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result is {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
