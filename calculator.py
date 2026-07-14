# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b


# def multiply(a, b):
#     return a * b


# def divide(a, b):
#     if b == 0:
#         return "Error! Division by zero is not allowed."
#     return a / b


# def modulus(a, b):
#     if b == 0:
#         return "Error! Division by zero is not allowed."
#     return a % b


# def power(a, b):
#     return a ** b


# def floor_division(a, b):
#     if b == 0:
#         return "Error! Division by zero is not allowed."
#     return a // b


# def menu():
#     print("\n========== PYTHON CALCULATOR ==========")
#     print("1. Addition (+)")
#     print("2. Subtraction (-)")
#     print("3. Multiplication (*)")
#     print("4. Division (/)")
#     print("5. Modulus (%)")
#     print("6. Power (**)")
#     print("7. Floor Division (//)")
#     print("8. Exit")


# while True:
#     menu()

#     try:
#         choice = int(input("\nEnter your choice (1-8): "))

#         if choice == 8:
#             print("\nThank you for using the Calculator!")
#             break

#         if choice not in range(1, 9):
#             print("Invalid choice! Please select between 1 and 8.")
#             continue

#         num1 = float(input("Enter First Number: "))
#         num2 = float(input("Enter Second Number: "))

#         if choice == 1:
#             result = add(num1, num2)

#         elif choice == 2:
#             result = subtract(num1, num2)

#         elif choice == 3:
#             result = multiply(num1, num2)

#         elif choice == 4:
#             result = divide(num1, num2)

#         elif choice == 5:
#             result = modulus(num1, num2)

#         elif choice == 6:
#             result = power(num1, num2)

#         elif choice == 7:
#             result = floor_division(num1, num2)

#         print("\nResult =", result)

#     except ValueError:
#         print("Invalid Input! Please enter numeric values.")
