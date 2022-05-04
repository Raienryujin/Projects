n = int(input("Please enter the number of terms: "))

def Fibonacci(n):
    i, n1, n2 = 0, 0, 1
    while i < n:
        print(n1)
        nth = n1 +n2
        n1 = n2
        n2 = nth
        i += 1

Fibonacci(n)