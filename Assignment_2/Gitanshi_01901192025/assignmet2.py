#assignment 2

# que 1 
sum = 0
for i in range(1, 11):
    sum += i
print("Sum of first 10 natural numbers =", sum)


# que 2
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)


#que 3 
n = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#que 4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if( a >= b and a >= c):
    largest = a
elif (b >= a and b >= c):
    largest = b
else:
    largest = c
print("Largest number =", largest)    


#que 5

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\n STUDENT RESULT ")
print("Name :", name)
print("Roll No :", roll)
print("Total Marks :", total)
print("Percentage :", percentage, "%")
print("Grade :", grade)