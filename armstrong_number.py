# taking input from user
num1 = int(input("Enter a number\n"))

s = 0

# find the sum of cube of each digit
temp = num1
while temp>0:
    digit = temp%10
    s += digit**3
    temp //= 10

# displaying the result
if num1 == sum:
    print(num1," is an Armstrong number.")
else:
    print(num1," is not an Armstrong number.")
