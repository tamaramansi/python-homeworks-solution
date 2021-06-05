# Homework 2
num1 = int(input("enter num1 : \n1.num1= "))
num2 = int(input("enter num2 : \n2.num2= "))
num3 = int(input("enter num3 : \n3.num3= "))
if num1>num2 and num1>num3:
    print( "The maximum number is: ",num1)
if num2>num1 and num2>num3 :
    print ("The maximum number is: ",num2)
if num3>num1 and num3>num2 :
    print("The maximum number is: ", num3)
if num1<num2 and num1<num3:
    print('The minimum number is :', num1)
if num2<num1 and num2<num3:
    print('The minimum number is :', num2)
if num3<num1 and num3<num2:
    print('The minimum number is :', num3) 
    
# Homework 3 
day = input("enter the day: \n1- Saturday \n2- Sunday \n3- Monday \n4- Tuesday \n5- Wednesday \n6- Thursday \n7- Friday \n")
if day =="1":
    print("The day is Saturday")
if day =="2":
    print("The day is Sunday")
if day =="3":
    print("The day is Monday")
if day =="4":
    print("The day is Tuesday")
if day =="5":
    print("The day is Wednesday")
if day =="6":
    print("The day is Thursday")
if day =="7":
    print("The day is Friday")