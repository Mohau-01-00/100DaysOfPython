#Calculator

#Add Function
def add(n1,n2):
    return n1+n2

#Subtract Function
def subtract(n1,n2):
    return n1-n2

#Multply Function
def multiply(n1,n2):
    return n1*n2

#Divide Function
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide

}
def calculator():

    num1=float(input("Please enter the first number :"))


    for symbol in operations:
        print(symbol)

    should_continue=True

    while should_continue:
        operation_symbol=input("Pick an operation from the line above :")
        num2=float(input("Please enter the second number :"))
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)

        print(f"{num1}{operation_symbol}{num2}={answer}")
        if input(f"Type 'y' to continue calculation with {answer} or type 'n' to exit:")=='y':
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()
