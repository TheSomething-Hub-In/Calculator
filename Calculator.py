ABC = input( "Hello! Please enter action. (+, -, *, /)") 
    

try: 
    a = float( input("Enter the first number:") )
    b = float ( input("Enter the second number:") )
except ValueError:
    print("Error! Please, write numbers!!!")

if ABC == "+":
    c = a + b 

elif ABC == "-":
    c = a - b

elif ABC == "*":
    c = a * b

elif ABC == "/":
    c = a / b 

else:
    print("Wrong! Invalid operation selected.")


print("Result: "+ str(c))