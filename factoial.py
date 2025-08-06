num = int(input("Enter a number to calculate its factorial: "))

for i in range(1, num + 1):
    if i == 1:
        factorial = 1
    else:
        factorial *= i

print("The factorial of {} is {}".format(num, factorial))