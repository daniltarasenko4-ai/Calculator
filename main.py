num1 = float(input("первое число?: "))
op = input("введите операцию (-, +, /, *):")
num2 = float(input("второе число?: "))
if op ==  "-": 
    print("result:", num1 - num2)
elif op ==  "+":
    print("result:", num1 + num2)  
elif op == "/" and num2 == 0:
    print("Operation is unavalible")
elif op== "/":
    print("result:", num1 / num2)    
elif op == "*":
    print("result:", num1 * num2)
else:
    print("Unknown Operation")