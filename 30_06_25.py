#Write a program to check if a number is positive or not
num = int(input("Enter a Number:"))
if num > 0 :
    print("Number is postive")
elif num < 0:
    print("Number is Negative")
else:
    print("number is Zero")
    
#Write a program to check if a number is even or odd.
num = int(input("Enter a Number:"))
if num % 2 == 0:
    print("Number is Even ")
else:
    print("Number is Odd")

# Write a program to find the largest among three numbers
num1 =  int(input("Enter The  1st Number: "))
num2 =  int(input("Enter The  2nd Number: "))
num3 =  int(input("Enter The  3rd Number: "))
if num1 > num2  and num1 > num3:
    print(f"{num1} Is Greater")
elif num2 > num1 and num2 > num3:
    print(f"{num2} Is Greater")
else:
    print(f"{num3} Is Greater")

# Find the factorial of a given number.
num = int(input("Enter a number:"))
fact = 1
for i in range(1,num+1,1):
    fact = fact * i
print(fact)

# Check whether a number is a prime number
num = int(input("Enter a Number:"))
for i in range(2,num):
    if num % i == 0:
        print("The Given Number Is  Not Prime")
        break
else:
        print("The  Given Number Is  Prime ")
        



