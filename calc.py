import math
import fractions
import numpy as np
def math_choice():
    if choice == 1:
        total = 0
        print("Addition")
        while True:
            num_str = float(input("> "))
            if num_str.lower() == 'done' or num_str == '':
                break
            try:
                num = float(num_str)
                total += num
            except ValueError:
                print("Invalid input")
        print(total)
    elif choice == 2:
        total = 0
        print("Subtraction")
        while True:
            num_str = float(input("> "))
            if num_str.lower() == 'done' or num_str == '':
                break
            try:
                num = float(num_str)
                total -= num
            except ValueError:
                print("Invalid input")
        print(total)
    elif choice == 3:
        total = 1
        print("Multiplication")
        while True:
            num_str = float(input("> "))
            if num_str.lower() == 'done' or num_str == '':
                break
            try:
                num = float(num_str)
                total *= num
            except ValueError:
                print("Invalid input")
        print(total)
    elif choice == 4:
        result = None
        print("Division")
        first_number_entered = False
        while True:
            num_str = float(input("> "))
            if num_str.lower() == 'done' or num_str == '':
                if not first_number_entered:
                    print("No numbers entered for division.")
                break
            try:
                num = float(num_str)
                if not first_number_entered:
                    result = num
                    first_number_entered = True
                else:
                    if num == 0:
                        print("Error: Cannot divide by zero! Please enter a non-zero number.")
                        continue
                    result /= num
            except ValueError:
                print("Invalid input")
        if first_number_entered:
            print(result)
    elif choice == 5:
        N = float(input("Enter a number to be put to the nth power:\n> "))
        m = float(input("Enter the nth power:\n> "))
        print(N**m)
    elif choice == 6:
        a = float(input("Enter a number to be rooted to the nth power:\n> "))
        n = float(input("Enter the nth root:\n> "))
        print(math.pow(a, n))
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
            matrix_a_row = int(input("Enter the number of rows for Matrix A:\n> "))
            matrix_a_col = int(input("Enter the number of columns for Matrix A:\n> "))
            matrix_b_row = int(input("Enter the number of rows for Matrix B:\n> "))
            matrix_b_col = int(input("Enter the number of columns for Matrix B:\n> "))
            if matrix_a_row == matrix_b_row and matrix_a_col == matrix_b_col:
                print("Enter values for Matrix A:")
                for i in range(matrix_a_row):
                    a_row = []
                    for j in range(matrix_a_col):
                        element = int(input(f"Enter element at ({i+1},{j+1}): "))
                        a_row.append(element)
                    matrix_a.append(a_row)
                print("Enter values for Matrix B:")
                for i in range(matrix_b_row):
                    b_row = []
                    for j in range(matrix_b_col):
                        element = int(input(f"Enter element at ({i+1},{j+1}): "))
                        b_row.append(element)
                    matrix_b.append(b_row)
                print("Matrix-A")
                n_matrix_a = np.array(matrix_a)
                for i in matrix_a:
                    print(i)
                print()
                print("Matrix-B")
                n_matrix_b = np.array(matrix_b)
                for i in matrix_b:
                    print(i)
                print("\nResult")
                print(np.add(n_matrix_a, n_matrix_b))
        elif N == 2:
            matrix_a = []
            matrix_b = []
            matrix_a_row = int(input("Enter the number of rows for Matrix A:\n> "))
            matrix_a_col = int(input("Enter the number of columns for Matrix A:\n> "))
            matrix_b_row = int(input("Enter the number of rows for Matrix B:\n> "))
            matrix_b_col = int(input("Enter the number of columns for Matrix B:\n> "))
            if matrix_a_row == matrix_b_row and matrix_a_col == matrix_b_col:
                print("Enter values for Matrix A:")
                for i in range(matrix_a_row):
                    a_row = []
                    for j in range(matrix_a_col):
                        element = int(input(f"Enter element at ({i+1},{j+1}): "))
                        a_row.append(element)
                    matrix_a.append(a_row)
                print("Enter values for Matrix B:")
                for i in range(matrix_b_row):
                    b_row = []
                    for j in range(matrix_b_col):
                        element = int(input(f"Enter element at ({i+1},{j+1}): "))
                        b_row.append(element)
                    matrix_b.append(b_row)
                print("Matrix-A")
                n_matrix_a = np.array(matrix_a)
                for i in matrix_a:
                    print(i)
                print()
                print("Matrix-B")
                n_matrix_b = np.array(matrix_b)
                for i in matrix_b:
                    print(i)
                print("\nResult")
                print(np.subtract(n_matrix_a, n_matrix_b))
        elif N == 3:
            matrix_a_row = int(input("Enter the number of rows for Matrix A:\n> "))
            matrix_a_col = int(input("Enter the number of columns for Matrix A:\n> "))
            matrix_b_row = int(input("Enter the number of rows for Matrix B:\n> "))
            matrix_b_col = int(input("Enter the number of columns for Matrix B:\n> "))
            if matrix_a_col == matrix_b_row:
                print("Enter values for Matrix A:")
                for i in range(matrix_a_row):
                    a_row = []
                    for j in range(matrix_a_col):
                        element = int(input(f"Enter element at ({i+1},{j+1}): "))
                        a_row.append(element)
                    matrix_a.append(a_row)
                print("Enter values for Matrix B:")
                for i in range(matrix_b_row):
                    b_row = []
                    for j in range(matrix_b_col):
                        element = int(input(f"Enter element at ({i+1},{j+1}): "))
                        b_row.append(element)
                    matrix_b.append(b_row)
                print("Matrix-A")
                n_matrix_a = np.array(matrix_a)
                for i in matrix_a:
                    print(i)
                print()
                print("Matrix-B")
                n_matrix_b = np.array(matrix_b)
                for i in matrix_b:
                    print(i)
                print("\nResult")
                print(np.multiply(n_matrix_a, n_matrix_b))
            else:
                print("Multiplication of these matrices is not possible (columns of matrix-a = row of matrix-b)")
        elif N == 4:
            matrix_a = []
            matrix_b = []
            matrix_a_row = int(input("Enter the number of rows for Matrix A:\n> "))
            matrix_a_col = int(input("Enter the number of columns for Matrix A:\n> "))
            matrix_b_row = int(input("Enter the number of rows for Matrix B:\n> "))
            matrix_b_col = int(input("Enter the number of columns for Matrix B:\n> "))
            if matrix_a_row == matrix_b_row and matrix_a_col == matrix_b_col:
                print("Enter values for Matrix A:")
                for i in range(matrix_a_row):
                    a_row = []
                    for j in range(matrix_a_col):
                        element = int(input(f"Enter element at ({i+1},{j+1}): "))
                        a_row.append(element)
                    matrix_a.append(a_row)
                print("Enter values for Matrix B:")
                for i in range(matrix_b_row):
                    b_row = []
                    for j in range(matrix_b_col):
                        element = int(input(f"Enter element at ({i+1},{j+1}): "))
                        b_row.append(element)
                    matrix_b.append(b_row)
                print("Matrix-A")
                n_matrix_a = np.array(matrix_a)
                for i in matrix_a:
                    print(i)
                print()
                print("Matrix-B")
                n_matrix_b = np.array(matrix_b)
                for i in matrix_b:
                    print(i)
                print("\nResult")
                print(np.divide(n_matrix_a, n_matrix_b))
    elif choice == 8:
        b = float(input("Enter the 'base' value:\n> "))
        x = float(input("Enter the 'exponent' value:\n> "))
        print(math.log(b, x))
    elif choice == 9:
        print("Options:")
        print("1. Degrees -> Radians")
        print("2. Radians -> Degrees")
        N = int(input("Choose a service:\n> "))
        while True:
            if N == 1:
                d = float(input("Enter the angle in degrees: "))
                r = float(d * (math.pi / 180))
                print(r)
            elif N == 2:
                r = float(input("Enter the angle in radians: "))
                d = float(r * (180 / math.pi))
                print(d)
    elif choice == 10:
        print("Finding the Lowest Common Multiple")
        a_str = float(input("Enter the first number:\n> "))
        b_str = float(input("Enter the second number:\n> "))
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
        a_str = float(input("Enter the first whole number:\n> "))
        b_str = float(input("Enter the second whole number:\n> "))
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
            print("The GCD of two zeros is undefined (or often considered 0).")
        elif a == 0:
            print(f"{abs(b)}")
        elif b == 0:
            print(f"{abs(a)}")
        else:
            result = hcf(abs(a), abs(b))
            print(result)
    elif choice == 12:
        print("Options:")
        print("1. Decimal -> Fraction")
        print("2. Fraction -> Decimal")
        N = int(input("Chose a service:\n> "))
        if (N == 1):
            a = float(input("Enter the decimal:\n> "))
            print(fractions.Fraction(a))
        elif (N == 2):
            a = int(input("Enter the numerator value:\n> "))
            b = int(input("Enter the denominator value:\n> "))
            print(a / b)
    elif choice == 13:
        print("Options:")
        print("1. Addition")
        print("2. Subraction")
        print("3. Multiplication")
        print("4. Division")
        N = int(input("Chose a service:\n> "))
        if N == 1:
            a = int(input("Enter the 'numerator' value of Fraction 1:\n> "))
            b = int(input("Enter the 'denominator' value of Fraction 1:\n> "))
            c = int(input("Enter the 'numerator' value of Fraction 2:\n> "))
            d = int(input("Enter the 'denominator' value of Fraction 2:\n> "))
            x = fractions.Fraction(a, b)
            y = fractions.Fraction(c, d)
            print(x + y)
        elif N == 2:
            a = int(input("Enter the 'numerator' value of Fraction 1:\n> "))
            b = int(input("Enter the 'denominator' value of Fraction 1:\n> "))
            c = int(input("Enter the 'numerator' value of Fraction 2:\n> "))
            d = int(input("Enter the 'denominator' value of Fraction 2:\n> "))
            x = fractions.Fraction(a, b)
            y = fractions.Fraction(c, d)
            print(x - y)
        elif N == 3:
            a = int(input("Enter the 'numerator' value of Fraction 1:\n> "))
            b = int(input("Enter the 'denominator' value of Fraction 1:\n> "))
            c = int(input("Enter the 'numerator' value of Fraction 2:\n> "))
            d = int(input("Enter the 'denominator' value of Fraction 2:\n> "))
            x = fractions.Fraction(a, b)
            y = fractions.Fraction(c, d)
            print(x * y)
        elif N == 4:
            a = int(input("Enter the 'numerator' value of Fraction 1:\n> "))
            b = int(input("Enter the 'denominator' value of Fraction 1:\n> "))
            c = int(input("Enter the 'numerator' value of Fraction 2:\n> "))
            d = int(input("Enter the 'denominator' value of Fraction 2:\n> "))
            x = fractions.Fraction(a, b)
            y = fractions.Fraction(c, d)
            print(x / y)
    elif choice == 20:
        a = int(input("Enter the 'n' value:\n> "))
        b = int(input("Enter the 'k' value:\n> "))
        c = a - b
        x = math.factorial(a)
        X = math.factorial(c)
        print(x / X)
    elif choice == 21:
        a = int(input("Enter the 'n' value: "))
        b = int(input("Enter the 'k' value: "))
        print(math.comb(a, b))
    elif choice == 22:
        x = int(input("Enter the 'x' value:\n> "))
        print(math.factorial(x))
    elif choice == 23:
        N = int(input("Enter the number to be factored:\n> "))
        for x in range (1, N + 1):
            if N % x == 0:
                print(x, end=" ")
    elif choice == 24:
        N = int(input("Enter a row of Pascal's Triangle:\n> "))
        for i in range(N + 1):
                print(math.comb(N, i), end=" ")
        print()
    elif choice == 25:
        n = int(input("Enter the number of Fibonacci Sequence to be displayed:\n> "))
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
    elif choice == 26:
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
            n = int(input("Enter the 'n' value:\n> "))
            if is_prime(n):
                print(f"Prime number.")
            else:
                print(f"Not a prime number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
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
    print("- Trigonomeric Functions -")
    print("14. Sine")
    print("15. Cosine")
    print("16. Tangent")
    print("17. Arcsine")
    print("18. Arccosine")
    print("19. Arctangent")
    print("- Advanced Formulas -")
    print("20. Calculate Permutations")
    print("21. Calculate Combinations")
    print("22. Calculate Factorials")
    print("- Niche Functions -")
    print("23. Factoring Numbers")
    print("24. Display Rows of Pascal's Triangle")
    print("25. Display Sequence of Fibonnaci Sequence")
    print("26. Determine if n is prime")
    global choice 
    choice = int(input("Your choice:\n> "))
    math_choice()
    pause()