# Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3
print("the sum of the three numbers is " + str(sum))
print("the product of the three numbers is " + str(product))
print("the average of the three numbers is " + str(average))