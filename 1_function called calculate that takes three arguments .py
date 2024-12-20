def calculate(num1,num2,operator):
    num1=int(input('enter first number:'))
    num2=int(input('enter second number:'))
    operator=input('enter operator:')
    if operator=='+':
        return num1+num2
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    elif operator=='/':
        if num2 !=0:
            return num1/num2
        else:
            return "division is not valid"
    else:
        return"invalid operator"
result=calculate(num1='',num2='',operator='')
# result=calculate(num1=num1,num2=num2,operator=operator)
print(result)

