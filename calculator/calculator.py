print("Basic calculator")
print("Operations")
print("1.Addiition +")
print("2.Subtraction -")
print("3.Multiplication *")
print("4.Division /")
operator=input("Enter the operator (+ - * /):")
number1=int(input("Enter 1st number:"))
number2=int(input("Enter 2nd operator:"))
if operator =="+":
    result=number1+number2
    print(round(result))
elif operator =="-":
    result=number1-number2
    print(round(result))
elif operator=="*":
    result=number1*number2
    print(round(result))
elif operator=="/":
    result=number1/number2
    print(result)
else:
    print("operator is invalid")
