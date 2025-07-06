def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def calculator():
    print("\n=== Simple Python Calculator ===")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            choice = input("\nEnter operation (1/2/3/4/5): ").strip()
            
            if choice == '5':
                print("Exiting calculator. Goodbye!")
                break
            
            if choice not in ('1', '2', '3', '4'):
                print("Invalid choice. Please try again.")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
        
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()