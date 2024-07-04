
print("      Welcome to the Simple Calculator!     ")
num1=float(input("enter the value of first number :"))
num2=float(input("enter the value of second number :"))


print("Operations available:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice=int(input("enter your choice from 1-4 :"))
if choice == 1:
   print( "the addition of given two numbers is:",num1 +num2)
elif choice == 2:
   print("the subtraction of given two numbers is:",num1-num2)
elif choice == 3:
   print("the multiplication of given two numbers is:",num1*num2)
elif choice ==4:
   print("the division of given two numbers is:",num1/num2)
else:
   print("invaild input")         


