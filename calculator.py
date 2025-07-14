def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
def show_menu():
     print("\n Calculator Menu")
     print("1.Add")
     print("2.subtract")
     print("3.multiply")
     print("4.divide")
     print("5.Exit")
while True:
    show_menu()
    choice = input("Enter your choice(1-5):")
    if choice == "5":
        print("Thank you for using the calculator!")
        break

    num1 = (input("Enter first number: "))
    num2 = (input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please try again.")
     
