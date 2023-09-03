# n = int(input("enter no of Fibonacci  numbers needed "))
n=50
num1 = 0
num2 = 1
next_number = num2

while next_number <= n:
	print(next_number, end=" \n")
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()
