import streamlit as st
from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def main():
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator!")
            continue

        print(f"The result is: {result}")

        quit = input("Do you want to quit? (Y/N): ")
        if quit == 'Y' or quit == 'y':
            break

main()
