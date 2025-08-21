import math
import fractions
import numpy as np
BLUE = '\033[34m'
GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'
def math_choice():
    if choice == 1:
        total = 0
        print("Addition")
        while True:
            num_str = float(input("> "))
            if num_str == 'done' or num_str == '':
                break
            try:
                num = float(num_str)
                total += num
            except ValueError:
                print(f"{RED}Invalid input{RESET}")
        print(total)
    elif choice == 2:
        total = 0
        print("Subtraction")
        while True:
            num_str = float(input("> "))
            if num_str == 'done' or num_str == '':
                break
            try:
                num = float(num_str)
                total -= num
            except ValueError:
                print(f"{RED}Invalid input{RESET}")
        print(total)
    elif choice == 3:
        total = 1
        print("Multiplication")
        while True:
            num_str = float(input("> "))
            if num_str == 'done' or num_str == '':
                break
            try:
                num = float(num_str)
                total *= num
            except ValueError:
                print(f"{RED}Invalid input{RESET}")
        print(total)
    elif choice == 4:
        result = None
        print("Division")
        first_number_entered = False
        while True:
            num_str = float(input("> "))
            if num_str == 'done' or num_str == '':
                if not first_number_entered:
                    print(f"{RED}No numbers entered for division{RESET}.")
                break
            try:
                num = float(num_str)
                if not first_number_entered:
                    result = num
                    first_number_entered = True
                else:
                    if num == 0:
                        print(f"{RED}Error{RESET}: Cannot divide by zero! Please enter a non-zero number.")
                        continue
                    result /= num
            except ValueError:
                print(f"{RED}Invalid input{RESET}")
        if first_number_entered:
            print(f"{GREEN}{result}{RESET}")
    elif choice == 5:
        N = float(input(f"Enter a {BLUE}number to be put to the nth power{RESET}:\n> "))
        m = float(input(f"Enter the {BLUE}nth power{RESET}:\n> "))
        print(f"{GREEN}{N**m}{RESET}")
    elif choice == 6:
        a = float(input(f"Enter a {BLUE}number to be rooted to the nth power{RESET}:\n> "))
        n = float(input(f"Enter the {BLUE}nth root{RESET}:\n> "))
        print(f"{GREEN}{a ** (1/n)}{RESET}")
    elif choice == 7:
        print("Options:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        N = int(input("Your choice:\n> "))
        if N == 1:
            matrix_a = []
            matrix_b = []
            matrix_a_row = int(input(f"Enter the {BLUE}number of rows{RESET} for {RED}Matrix A{RESET}:\n> "))
            matrix_a_col = int(input(f"Enter the {BLUE}number of columns{RESET} for {RED}Matrix A{RESET}:\n> "))
            matrix_b_row = int(input(f"Enter the {BLUE}number of rows{RESET} for {RED}Matrix B{RESET}:\n> "))
            matrix_b_col = int(input(f"Enter the {BLUE}number of columns{RESET} for {RED}Matrix B{RESET}:\n> "))
            if matrix_a_row == matrix_b_row and matrix_a_col == matrix_b_col:
                print(f"Enter values for {BLUE}Matrix A{RESET}:")
                for i in range(matrix_a_row):
                    a_row = []
                    for j in range(matrix_a_col):
                        element = int(input(f"Enter element at {BLUE}({i+1},{j+1}){RESET}:\n> "))
                        a_row.append(element)
                    matrix_a.append(a_row)
                print(f"Enter values for {BLUE}Matrix B{RESET}:")
                for i in range(matrix_b_row):
                    b_row = []
                    for j in range(matrix_b_col):
                        element = int(input(f"Enter element at {BLUE}({i+1},{j+1}){RESET}:\n> "))
                        b_row.append(element)
                    matrix_b.append(b_row)
                print(f"{RED}Matrix A{RESET}")
                n_matrix_a = np.array(matrix_a)
                for i in matrix_a:
                    print(i)
                print()
                print(f"{RED}Matrix B{RESET}")
                n_matrix_b = np.array(matrix_b)
                for i in matrix_b:
                    print(i)
                print("\nResult")
                print(f"{GREEN}{np.add(n_matrix_a, n_matrix_b)}{RESET}")
        elif N == 2:
            matrix_a = []
            matrix_b = []
            matrix_a_row = int(input(f"Enter the {BLUE}number of rows{RESET} for {RED}Matrix A{RESET}:\n> "))
            matrix_a_col = int(input(f"Enter the {BLUE}number of columns{RESET} for {RED}Matrix A{RESET}:\n> "))
            matrix_b_row = int(input(f"Enter the {BLUE}number of rows{RESET} for {RED}Matrix B{RESET}:\n> "))
            matrix_b_col = int(input(f"Enter the {BLUE}number of columns{RESET} for {RED}Matrix B{RESET}:\n> "))
            if matrix_a_row == matrix_b_row and matrix_a_col == matrix_b_col:
                print(f"Enter values for {BLUE}Matrix A{RESET}:")
                for i in range(matrix_a_row):
                    a_row = []
                    for j in range(matrix_a_col):
                        element = int(input(f"Enter element at {BLUE}({i+1},{j+1}){RESET}:\n> "))
                        a_row.append(element)
                    matrix_a.append(a_row)
                print(f"Enter values for {BLUE}Matrix B{RESET}:")
                for i in range(matrix_b_row):
                    b_row = []
                    for j in range(matrix_b_col):
                        element = int(input(f"Enter element at {BLUE}({i+1},{j+1}){BLUE}:\n> "))
                        b_row.append(element)
                    matrix_b.append(b_row)
                print(f"{RED}Matrix A{RESET}")
                n_matrix_a = np.array(matrix_a)
                for i in matrix_a:
                    print(i)
                print()
                print(f"{RED}Matrix B{RESET}")
                n_matrix_b = np.array(matrix_b)
                for i in matrix_b:
                    print(i)
                print("\nResult")
                print(f"{GREEN}{np.subtract(n_matrix_a, n_matrix_b)}{RESET}")
        elif N == 3:
            matrix_a = []
            matrix_b = []
            matrix_a_row = int(input(f"Enter the {BLUE}number of rows{RESET} for {RED}Matrix A{RESET}:\n> "))
            matrix_a_col = int(input(f"Enter the {BLUE}number of columns{RESET} for {RED}Matrix A{RESET}:\n> "))
            matrix_b_row = int(input(f"Enter the {BLUE}number of rows{RESET} for {RED}Matrix B{RESET}:\n> "))
            matrix_b_col = int(input(f"Enter the {BLUE}number of columns{RESET} for {RED}Matrix B{RESET}:\n> "))
            if matrix_a_col == matrix_b_row:
                print(f"Enter values for {BLUE}Matrix A{RESET}:")
                for i in range(matrix_a_row):
                    a_row = []
                    for j in range(matrix_a_col):
                        element = int(input(f"Enter element at {BLUE}({i+1},{j+1}){RESET}:\n> "))
                        a_row.append(element)
                    matrix_a.append(a_row)
                print(f"Enter values for {BLUE}Matrix B{RESET}:")
                for i in range(matrix_b_row):
                    b_row = []
                    for j in range(matrix_b_col):
                        element = int(input(f"Enter element at {BLUE}({i+1},{j+1}){RESET}:\n> "))
                        b_row.append(element)
                    matrix_b.append(b_row)
                print(f"{BLUE}Matrix A{RESET}")
                n_matrix_a = np.array(matrix_a)
                for i in matrix_a:
                    print(i)
                print()
                print(f"{BLUE}Matrix B{RESET}")
                n_matrix_b = np.array(matrix_b)
                for i in matrix_b:
                    print(i)
                print("\nResult")
                print(f"{GREEN}{np.dot(n_matrix_a, n_matrix_b)}{RESET}")
            else:
                print(f"Multiplication of these matrices is {RED}not possible{RESET} (columns of matrix-a = row of matrix-b)")
        elif N == 4:
            matrix_a = []
            matrix_b = []
            matrix_a_row = int(input(f"Enter the {BLUE}number of rows{RESET} for {RED}Matrix A{RESET}:\n> "))
            matrix_a_col = int(input(f"Enter the {BLUE}number of columns{RESET} for {RED}Matrix A{RESET}:\n> "))
            matrix_b_row = int(input(f"Enter the {BLUE}number of rows{RESET} for {RED}Matrix B{RESET}:\n> "))
            matrix_b_col = int(input(f"Enter the {BLUE}number of columns{RESET} for {RED}Matrix B{RESET}:\n> "))
            if matrix_a_row == matrix_b_row and matrix_a_col == matrix_b_col:
                print(f"Enter values for {BLUE}Matrix A{RESET}:")
                for i in range(matrix_a_row):
                    a_row = []
                    for j in range(matrix_a_col):
                        element = int(input(f"Enter element at {BLUE}({i+1},{j+1}){RESET}:\n> "))
                        a_row.append(element)
                    matrix_a.append(a_row)
                print(f"Enter values for {BLUE}Matrix B{RESET}:")
                for i in range(matrix_b_row):
                    b_row = []
                    for j in range(matrix_b_col):
                        element = int(input(f"Enter element at {BLUE}({i+1},{j+1}){RESET}:\n> "))
                        b_row.append(element)
                    matrix_b.append(b_row)
                print(f"{BLUE}Matrix A{RESET}")
                n_matrix_a = np.array(matrix_a)
                for i in matrix_a:
                    print(i)
                print()
                print(f"{BLUE}Matrix B{RESET}")
                n_matrix_b = np.array(matrix_b)
                for i in matrix_b:
                    print(i)
                print("\nResult")
                print(f"{GREEN}{np.divide(n_matrix_a, n_matrix_b)}{RESET}")
    elif choice == 8:
        b = float(input(f"Enter the {BLUE}base value{RESET}:\n> "))
        x = float(input(f"Enter the {BLUE}exponent value{RESET}:\n> "))
        print(math.log(b, x))
    elif choice == 9:
        print("Options:")
        print("1. Degrees -> Radians")
        print("2. Radians -> Degrees")
        N = int(input("Choose a service:\n> "))
        while True:
            if N == 1:
                d = float(input(f"Enter the {BLUE}angle in degrees{RESET}:\n> "))
                r = float(d * (math.pi / 180))
                print(r)
            elif N == 2:
                r = float(input(f"Enter the {BLUE}angle in radians{RESET}:\n> "))
                d = float(r * (180 / math.pi))
                print(d)
    elif choice == 10:
        print("Finding the Lowest Common Multiple")
        a_str = float(input(f"Enter the {BLUE}first integar{RESET}:\n> "))
        b_str = float(input(f"Enter the {BLUE}second number{RESET}:\n> "))
        a = int(a_str)
        b = int(b_str)
        def lcm(a, b):
            L = a if a > b else b
            while L <= a * b:
                if L % a == 0 and L % b == 0:
                    return L
                L += 1
            return a * b
        print(lcm(a, b))
    elif choice == 11:
        a_str = float(input(f"Enter the {BLUE}first integar{RESET}:\n> "))
        b_str = float(input(f"Enter the {BLUE}second integar{RESET}:\n> "))
        a = int(a_str)
        b = int(b_str)
        def hcf(a, b):
            a = abs(a)
            b = abs(b)
            H = a if a < b else b
            while H >= 1:
                if a % H == 0 and b % H == 0:
                    return H
                H -= 1
            return 1
        if a == 0 and b == 0:
            print(f"The GCD of two zeros is {RED}undefined{RESET} (or often considered 0).")
        elif a == 0:
            print(f"{GREEN}{abs(b)}{RESET}")
        elif b == 0:
            print(f"{GREEN}{abs(a)}{RESET}")
        else:
            result = hcf(abs(a), abs(b))
            print(f"{GREEN}{result}{RESET}")
    elif choice == 12:
        print("Options:")
        print("1. Decimal -> Fraction")
        print("2. Fraction -> Decimal")
        N = int(input("Chose a service:\n> "))
        if (N == 1):
            a = float(input(f"Enter the {BLUE}decimal{RESET}:\n> "))
            print(fractions.Fraction(a))
        elif (N == 2):
            a = int(input(f"Enter the {BLUE}numerator value{RESET}:\n> "))
            b = int(input(f"Enter the {BLUE}denominator value{RESET}:\n> "))
            print(a / b)
    elif choice == 13:
        print("Options:")
        print("1. Addition")
        print("2. Subraction")
        print("3. Multiplication")
        print("4. Division")
        N = int(input("Chose a service:\n> "))
        if N == 1:
            a = int(input(f"Enter the {BLUE}numerator value{RESET} of {RED}Fraction 1{RESET}:\n> "))
            b = int(input(f"Enter the {BLUE}denominator value{RESET} of {RED}Fraction 1{RESET}:\n> "))
            c = int(input(f"Enter the {BLUE}numerator value{RESET} of {RED}Fraction 2:{RESET}\n> "))
            d = int(input(f"Enter the {BLUE}denominator value{RESET} of {RED}Fraction 2:{RESET}\n> "))
            x = fractions.Fraction(a, b)
            y = fractions.Fraction(c, d)
            print(f"{GREEN}{x + y}{RESET}")
        elif N == 2:
            a = int(input(f"Enter the {BLUE}numerator value{RESET} of {RED}Fraction 1{RESET}:\n> "))
            b = int(input(f"Enter the {BLUE}denominator value{RESET} of {RED}Fraction 1{RESET}:\n> "))
            c = int(input(f"Enter the {BLUE}numerator value{RESET} of {RED}Fraction 2{RESET}:\n> "))
            d = int(input(f"Enter the {BLUE}denominator value{RESET} of {RED}Fraction 2{RESET}:\n> "))
            x = fractions.Fraction(a, b)
            y = fractions.Fraction(c, d)
            print(f"{GREEN}{x - y}{RESET}")
        elif N == 3:
            a = int(input(f"Enter the {BLUE}numerator value{RESET} of {RED}Fraction 1{RESET}:\n> "))
            b = int(input(f"Enter the {BLUE}denominator value{RESET} of {RED}Fraction 1{RESET}:\n> "))
            c = int(input(f"Enter the {BLUE}numerator value{RESET} of {RED}Fraction 2{RESET}:\n> "))
            d = int(input(f"Enter the {BLUE}denominator value{RESET} of {RED}Fraction 2{RESET}:\n> "))
            x = fractions.Fraction(a, b)
            y = fractions.Fraction(c, d)
            print(f"{GREEN}{x * y}{RESET}")
        elif N == 4:
            a = int(input(f"Enter the {BLUE}numerator value{RESET} of {RED}Fraction 1{RESET}:\n> "))
            b = int(input(f"Enter the {BLUE}denominator value{RESET} of {RED}Fraction 1{RESET}:\n> "))
            c = int(input(f"Enter the {BLUE}numerator value{RESET} of {RED}Fraction 2{RESET}:\n> "))
            d = int(input(f"Enter the {BLUE}denominator value{RESET} of {RED}Fraction 2{RESET}:\n> "))
            x = fractions.Fraction(a, b)
            y = fractions.Fraction(c, d)
            print(f"{GREEN}{x / y}{RESET}")
    elif choice == 14:
        print("Options:")
        print("1. Radians")
        print("2. Degrees")
        N = int(input("Your choice:\n> "))
        if N == 1:
            X = float(input(f"Enter the {BLUE}degree in Radians{RESET}:\n> "))
            x = math.degrees(X)
            print(f"Sine: {GREEN}{math.sin(x)}{RESET}")
            print(f"Cosine: {GREEN}{math.cos(x)}{RESET}")
            print(f"Tangent: {GREEN}{math.tan(x)}{RESET}")
            print(f"Arcsine: {GREEN}{math.asin(x)}{RESET}")
            print(f"Arccosine: {GREEN}{math.acos(x)}{RESET}")
            print(f"Arctangent: {GREEN}{math.atan(x)}{RESET}")
            print(f"Hyperbolic Sine: {GREEN}{math.sinh(x)}{RESET}")
            print(f"Hyperbolic Cosine: {GREEN}{math.cosh(x)}{RESET}")
            print(f"Hyperbolic Tangent: {GREEN}{math.tanh(x)}{RESET}")
        elif N == 2:
            x = float(input(f"Enter the {BLUE}degree in Degrees{RESET}:\n> "))
            print(f"Sine: {GREEN}{math.sin(x)}{RESET}")
            print(f"Cosine: {GREEN}{math.cos(x)}{RESET}")
            print(f"Tangent: {GREEN}{math.tan(x)}{RESET}")
            print(f"Arcsine: {GREEN}{math.asin(x)}{RESET}")
            print(f"Arccosine: {GREEN}{math.acos(x)}{RESET}")
            print(f"Arctangent: {GREEN}{math.atan(x)}{RESET}")
            print(f"Hyperbolic Sine: {GREEN}{math.sinh(x)}{RESET}")
            print(f"Hyperbolic Cosine: {GREEN}{math.cosh(x)}{RESET}")
            print(f"Hyperbolic Tangent: {GREEN}{math.tanh(x)}{RESET}")
    elif choice == 15:
        a = int(input(f"Enter the {BLUE}n value{RESET}:\n> "))
        b = int(input(f"Enter the {BLUE}k value{RESET}:\n> "))
        x = math.factorial(a)
        X = math.factorial(a - b)
        print(f"{GREEN}{x / X}{RESET}")
    elif choice == 16:
        a = int(input(f"Enter the {BLUE}n value{RESET}: "))
        b = int(input(f"Enter the {BLUE}k value{RESET}: "))
        print(f"{GREEN}{math.comb(a, b)}{RESET}")
    elif choice == 17:
        x = int(input(f"Enter the {BLUE}x value{RESET}:\n> "))
        print(f"{GREEN}{math.factorial(x)}{RESET}")
    elif choice == 18:
        print("Lateral Surface Area")
        print("Options:")
        print("1. Cube")
        print("2. Rectangular Prism")
        print("3. Triangular Prism")
        print("4. Cone")
        print("5. ")
        N = input("Your choice:\n> ")
        if N == 1:
            a = input("")
        elif N == 2:
            a = input("")
        elif N == 3:
            a = input("")
        elif N == 4:
            r = input("Enter the ")
    elif choice == 21:
        N = int(input(f"Enter the {BLUE}number to be factored{RESET}:\n> "))
        for x in range (1, N + 1):
            if N % x == 0:
                print(x, end=" ")
    elif choice == 22:
        N = int(input(f"Enter a {BLUE}row of Pascal's Triangle{RESET}:\n> "))
        for i in range(N + 1):
                print(math.comb(N, i), end=" ")
        print()
    elif choice == 23:
        n = int(input(f"Enter the {BLUE}number of Fibonacci Sequence{RESET} to be displayed:\n> "))
        a = 0
        b = 1
        next = b  
        count = 1
        while count <= n:
            print(next, end=" ")
            count += 1
            a, b = b, next
            next = a + b
        print()
    elif choice == 24:
        def is_prime(num):
            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
            return True
        try:
            n = int(input(f"Enter the {BLUE}n value{RESET}:\n> "))
            if is_prime(n):
                print(f"{GREEN}Prime number{RESET}.")
            else:
                print(f"{RED}Not a prime number{RESET}.")
        except ValueError:
            print(f"{RED}Invalid input{RESET}. Please enter an integer.")
def pause():
    x = input("")
    while x == True:
        continue
while True:
    print("")
    print("Options:")
    print("- Basic Arithmetic -")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divison")
    print("5. Calculate Powers")
    print("6. Calculate Roots")
    print("- Advanced Maths -")
    print("7. Solving Matrices")
    print("8. Calculating Logarithms")
    print("9. Convert Degrees and Radians")
    print("- Math Foundations -")
    print("10. Find the Least Common Multiple")
    print("11. Find the Greatest Common Multiple")
    print("12. Convert Decimals and Fractions")
    print("13. Basic Arithmetic with Fractions")
    print("14. Trigonomic Functions")
    print("- Advanced Formulas -")
    print("15. Calculate Permutations")
    print("16. Calculate Combinations")
    print("17. Calculate Factorials")
    print("18. Lateral Surface Area")
    print("19. Total Surface Area")
    print("20. Volume")
    print("- Niche Functions -")
    print("21. Factoring Numbers")
    print("22. Display Rows of Pascal's Triangle")
    print("23. Display Sequence of Fibonnaci Sequence")
    print("24. Determine if n is prime")
    global choice 
    choice = int(input("Your choice:\n> "))
    math_choice()
    pause()
