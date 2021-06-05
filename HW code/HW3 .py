# HW1 length and breadth of a rectangular 
Len=int(input("enter the length = "))
Bre=int(input("enter the breadth = "))
if Len == Bre:
    print("it's square")
else:
  print("it's rectangular ")    
  
  
#HW2 company gives bonus 
salary=int(input("enter your salary : "))
expYears= int(input("enter your experience years :"))
if expYears > 5:
    bonus= salary * 0.1  # bonus is 10% of the salary 
    print ("the amount of your bonus = ", bonus)
else:
    print( "no bonus for you ")
    

#HW3 absolute value of numbers 
num=int(input("enter the number = "))
if num < 0:
    num*=-1
    print("the absolute value = ",num)
else:
    print("the absolute value = ",num)
    
#HW4 Ages 
age=int(input(" put your age : "))
if age> 0 and age <= 14 :  # age between (0-14)
    print("you're in the Children Category")
elif age>=15 and age<= 24: # age between (15-24)
        print("you're in the Youth Category")
elif age>=25 and age<=64:  # age between (25-64)
        print("you're in the Adult Category")
elif age > 65:  # age more than 65 
        print("you're in Senior Category")