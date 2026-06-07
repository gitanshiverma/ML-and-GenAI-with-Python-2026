
#que 1
def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()

#que 2
def sum_n(n):
    return n * (n + 1) // 2

n = int(input("Enter N: "))
print("Sum =", sum_n(n))


#que 3
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev

num = int(input("Enter number: "))
print("Reverse =", reverse_number(num))


#que 4
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

num = int(input("Enter number: "))
print("Digits =", count_digits(num))

#que 5
def palindrome(n):
    original = n
    rev = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    return original == rev

num = int(input("Enter number: "))

if palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")

 #que 6   

def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter terms: "))
fibonacci(n)

#que 7
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Result =", add(a, b))
elif choice == 2:
    print("Result =", subtract(a, b))
elif choice == 3:
    print("Result =", multiply(a, b))
elif choice == 4:
    print("Result =", divide(a, b))
else:
    print("Invalid Choice")


#que 8
    file = open("student.txt", "w")

name = input("Enter Name: ")
roll = input("Enter Roll No: ")
marks = input("Enter Marks: ")

file.write("Name: " + name + "\n")
file.write("Roll No: " + roll + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("Data stored successfully.")

#que9

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()

#que 10 

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")


    
 # que 11   
    
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("Enter Name: ")
marks = float(input("Enter Marks: "))

s = Student(name, marks)

s.display()