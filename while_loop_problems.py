# Print all numbers from 1 to 100 using a while loop
num=1
while num<=100:
    print(num)
    num+=1
# Simulate a fan regulator by printing the numbers from 1 to 5 and then back to 1 using a while loop
regulator = 1
up = True

while True:
    print(regulator)

    if up:
        if regulator == 5:
            up = False
        else:
            regulator += 1
    else:
        if regulator == 1:
            break
        regulator -= 1

# Print all even numbers from 1 to 100 using a while loop
nums=1
while nums<=100:
    if nums%2==0:
        print(nums)
    nums+=1
# Print all odd numbers from 1 to 100 using a while loop
nums=1
while nums<=100:
    if nums%2!=0:
        print(nums)
    nums+=1
# Write a program to find the sum of numbers from 1 to n (where n is a user-inputted number) using a while loop
n=int(input("Enter number: "))
c=1
total=0

while c<=n:
    total+=c
    c+=1
print(total)
# Calculate the factorial of a given number using a while loop
num=int(input("Enter number: "))
factorial_number=1
c=1
while c<=num:
    factorial_number*=c
    c+=1
print(factorial_number)
# Reverse a given number using a while loop
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10        # Get the last digit
    reverse = reverse * 10 + digit
    num = num // 10         # Remove the last digit

print("Reversed number:", reverse)


# Check whether a given number is a palindrome or not using a while loop
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
# Count the number of digits in a given number using a while loop
num = int(input("Enter a number: "))

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num = num // 10

print("Number of digits:", count)
# Find the sum of the digits of a given number in Python using a while loop
num = int(input("Enter a number: "))

sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10

print("Sum of digits:", sum_of_digits)
