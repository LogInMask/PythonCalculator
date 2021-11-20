num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
op = (input("Input operation: "))

sum1 = num1 + num2
sum2 = num1 - num2
sum3 = num1 * num2
sum4 = num1 / num2

if op == "+":
    print(sum1)
if op == "-":
    print(sum2)
if op == "*":
    print(sum3)
if op == "/":
    print(sum4)
