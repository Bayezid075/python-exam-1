while True:
    user_operation_mode = input('''
1 for Add(+)
2 for Substraction (-)
3 for Multiplication (*)
4 for Division (/)
5 for Modulus (%)
--> Select your Mode : 
''')
    user_operation_mode = int(user_operation_mode)
    if user_operation_mode <= 5  and user_operation_mode  != 0 :
        break
    else:
        print("Wrong Operation Mode | Please Choose from above")

user_first_number = float(input("Inter Your First Number : "))
user_second_number = float(input("Inter Your second Number : "))

def addition(a = user_first_number, b = user_second_number):
    print(f"{a} + {b} = {a+b}")
def subtraction(a = user_first_number, b = user_second_number):
    print(f"{a} - {b} = {a-b}")
def multiplication(a = user_first_number, b = user_second_number):
    print(f"{a} * {b} = {a*b}")
def division(a = user_first_number, b = user_second_number):
    if a == 0 or b ==0 : # error handler
        print("Division cannot be performed by 0, please try another number")
    else:
        print(f"{a} / {b} = {a/b}")
def modulus(a = user_first_number, b = user_second_number):
    print(f"{a} / {b} = {a/b}")

if user_operation_mode == 1:
    addition()
elif user_operation_mode == 2:
    subtraction()
elif user_operation_mode == 3:
    multiplication()
elif user_operation_mode == 4:
    division()
elif user_operation_mode == 5:
    modulus()



