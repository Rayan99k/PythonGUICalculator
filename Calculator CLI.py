import math
import tkinter

import random
variable1 = random.randint(0, 100)
variable2 = random.randint(0, 100)
variable3 = random.randint(0, 100)
def sinelaw (A, a, B, b, C, c):
    return(math.sin(A) / a, math.sin(B) / b, math.sin(C) / c)
def  solve(a, b, c):
    return((-1)* b + math.sqrt(b**2-4*a*c))/2*a
    return((-1)* b - math.sqrt(b**2-4*a*c))/2*a
def  add(x, y):
    return x + y
def  subtract(x, y):
    return x - y
def  multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def Reset(prompt):
    ans = input(prompt)
    if ans.upper() == "Y":
        return True
    else:
        return False
    
restart = True
while restart:
    print ("Welcome to Rayan's basic calculator. Select operation...")
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print ("4. Division")
    print ("5. Exponents")
    print ("6. Square Root")
    print ("7. Quadratic Solver")
    print ("8. Sine law")
    print ("9. Randomly Generated Quadratics")


    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/0)")
    if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6' and choice != '7' and choice!= '8' and choice != '9':
        print ("The number you entered is not on the list!")


    if choice == '1':
        num1 = int(input("Enter first number:  "))
        num2 = int(input("Enter second number:  "))
        print(num1,"+",num2,"=", add(num1,num2))
        
    elif choice == '2':
        num1 = int(input("Enter first number:  "))
        num2 = int(input("Enter second number:  "))
        print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
        num1 = int(input("Enter first number:  "))
        num2 = int(input("Enter second number:  "))
        print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
        num1 = int(input("Enter first number:  "))
        num2 = int(input("Enter second number:  "))
        print(num1,"/",num2,"=", divide(num1,num2))

    elif choice == '5':
        num1 = int(input("Enter the base number:  "))
        num2 = int(input("Enter the exponent:  "))
        print(pow(num1, num2))

    elif choice == '6':
        num1 = int(input("Enter the base number:  "))
        print(math.sqrt(num1))

    elif choice == '7':
        print("ax^2 + bx + c = 0")
        a = int(input("Enter the value of A: "))
        b = int(input("Enter the value of B: "))
        c = int(input("Enter the value of C: "))
        x = int
        if not a:
                print ("Error, if variable A equals 0, then the equation is NOT a quadratic")
                
        else:
            d = pow(b, 2)-(4*a*c)
            q = (-b + math.sqrt(d))/(2*a)
            q2 = (-b - math.sqrt(d))/(2*a) 
            print("x = " + str(q))
        if q != q2:
            print("x = " + str(q2))
            if d < 0:
                print ("Error: The Discriminant is of negative value and the solutions are non-real")

    elif choice == '8':
        choice = input("Would you like to find an angle or a side measurement? (Angle / Side)")
        if choice == 'Angle' or choice == 'angle':
                print("A = sin^-1 * ((a * sin *B) / b)")
                a = int(input("Enter the value of a: "))
                B = int(input("Enter the value of B: "))
                b = int(input("Enter the value of b: "))
                A = math.asin((a * math.sin(B)) / b)
                print(A)
        if choice == 'Side' or choice == 'side':
                print("a = (b * sin * A) / (sin * B)")
                A = int(input("Enter the value of A: "))
                B = int(input("Enter the value of B: "))
                b = int(input("Enter the value of b: "))
                a = b * math.sin(A) / math.sin(B)
                print(a)

    elif choice == '9':
        print("ax^2 + bx + c")
        variable1 = random.randint(0, 100)
        variable2 = random.randint(0, 100)
        variable3 = random.randint(0, 100)
        a = variable1
        b = variable2
        c = variable3
        print(a, b, c)



    else:
        print("Invalid input")


    restart = Reset("Would you like to restart the application? (Y / N)")

        
