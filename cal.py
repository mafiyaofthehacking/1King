
print('''
1. ADD
2. SUBSTRACT
3. MULTIPLY
4. DEVIDED''')
print("Select an operation to perform ~ ")
operation = input()
if operation == "1" :
	num1 = input("Enter first number  : ")
	num2 = input("Enter second number : ")
	print("---------------------------------------------------")
	print("The sum is          = " + str(int(num1) + int(num2)))
elif operation == "2" :
	num1 = input("Enter first number  :")
	num2 = input("Enter second number :")
	print("---------------------------------------------------")
	print("The diffrent is = " + str(int(num1) - int(num2)))
elif operation == "3" :
	num1 = input("Enter first number  :")
	num2 = input("Enter second number :")
	print("---------------------------------------------------")
	print("The product is  " + str(int(num1) * int(num2)))
if operation == "4" :
	num1 = input("Enter first number  :")
	num2 = input("Enter second number :")
	print("---------------------------------------------------")
	print("The result is " + str(int(num1) / int(num2)))
else :
	print("Invalid entry")