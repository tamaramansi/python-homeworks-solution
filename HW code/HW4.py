#HW1 the factorial of an input number

num= int(input("enter the number = "))
def factorial(n):
     if (n==0):
        return 1;
     return n*factorial(n-1)
print("factorial of ",num,'is ', factorial(num))

# HW2 the power of an input number
x=0
while x>=0:
   baseNum=int(input("enter base value = "))
   expNum=int(input('enter exponent value = '))
   Num= baseNum**expNum
   print (baseNum,"^",expNum,"= ", Num)
   x+=1

#HW3  rectangular area 

length=float(input("the length of the rectangular = "))
width= float(input("the width of the rectangular = "))
area= length*width
print("the area = ",area)
x=0
while x<=width:
    print("|")
    x+=1

#HW4 Average of numbers 
x=0
Sum=0
while True:
    numb=input("enter your number  =")
    if numb=="q":
      break 
  
    Sum+=float(numb)
    x+=1
avg=Sum/x 
print("Average = ",avg)




#HW5 
x=0
Numb=int(input("insert an int number = "))
while x<=10:
    y=Numb*x
    print(Numb,"*", x,"= ",y)
    x+=1 
























