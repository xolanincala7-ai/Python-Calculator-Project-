# Hello, For this Project we simulate our Python script as a Calculator

# Using principles of OOP we start with defining a Calculator class
# With methods that perform basic operations (addition, subtraction, multiplication, division).
# We now extend it with power, root functions, and a constant (pi), i import math module for these.
# We also store every answer in a list until the program exits or an error occurs.

import math

class Calculator:
    def __init__(self):
        self.answers = []

    def add(self, a, b):    
        return a + b
    
    def subtract(self, a, b): 
        return a - b

    def multiply(self, a, b):    
        return a * b 
    
    def divide(self, a, b):         
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of a negative number")
        return x ** 0.5

    def cube_root(self, x):
        return x ** (1/3)

    def nth_root(self, x, n):
        if n == 0:
            raise ValueError("Root degree cannot be zero")
        return x ** (1/n)

    def get_pi(self):
        return math.pi

# Moving to the methods that handle User Interaction 

    def run(self):
        while True:                             # Infinite run loop for calc
            print("\n--- X_Calculator Menu")    # Menu printing
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Power (x^y)")
            print("6. Square Root")
            print("7. Cube Root")
            print("8. Nth Root")
            print("9. Constant Pi")
            
            choice = input("Enter choice (1-9): ")      # User Choice
        
# Start of the try block and Operations using the methods    
            try:
                if choice in ['1','2','3','4','5','8']:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                elif choice in ['6','7']:
                    num1 = float(input("Enter the number: "))

                # Perform operation based on choice
                if choice == '1':
                    result = self.add(num1, num2)
                elif choice == '2':
                    result = self.subtract(num1, num2)
                elif choice == '3':
                    result = self.multiply(num1, num2)
                elif choice == '4':
                    result = self.divide(num1, num2)
                elif choice == '5':
                    result = self.power(num1, num2)
                elif choice == '6':
                    result = self.square_root(num1)
                elif choice == '7':
                    result = self.cube_root(num1)
                elif choice == '8':
                    result = self.nth_root(num1, num2)
                elif choice == '9':
                    result = self.get_pi()
                else:
                    print("Invalid choice.")
                    continue

# The start of our except block, for handling non-numeric, zero-division,
# overflow, and other errors  
# I have also stored the result in the answers list . I did this because when performing multiple 
# operations i kept forgetting the previous ans. 
            except ValueError:
                print("Error: Invalid input. Enter numeric values")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
            except OverflowError:
                print("Error: Result too large to calculate.")
            except Exception as e:
                print(f"Unexpected error: {e}")
            else:
    
                self.answers.append(result)
                print(f"Answer {len(self.answers)}: {result}")
                print("Operation completed successfully")
            finally:
                again = input("Do you want to perform another operation? (yes/no): ").lower()
                if again != 'yes':
                    print("Exiting X_calculator. Goodbye!")
                    print("All stored answers:", self.answers)
                    break

# We create the Calculator() instance as X_Calc
x_calc = Calculator()
x_calc.run()

# We are done thank you. 