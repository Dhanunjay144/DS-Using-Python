print("Checking with integer types")

num1 = 10
num2 = num1

print("Values of num1 and num2")
print("Value of num1:", num1)
print("Value of num2:", num2)

print("\nlocation of num1:", id(num1))
print("location of num2:", id(num2))

num2 = 20

print("After updating num2")
print("Value of num1:", num1)
print("Value of num2:", num2)

print("\nlocation of num1:", id(num1))
print("location of num2:", id(num2))