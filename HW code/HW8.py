#HW1 Max
def max(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    if n2>n1 and n2>n3:
        return n2
    return n3

maximum= max(5,2,6)
maximum1=max(9,5,2)
maximum2=max(1,8,4)

#HW2 Min
def min(n1,n2,n3):
    if n1<n2 and n1<n3:
        return n1
    if n2<n1 and n2<n3:
        return n2
Min= min(5,2,6)
Min1=min(9,5,2)
Min2=min(1,8,4)

#HW3 name and age
def info():
    name= input("name: ")
    age= int(input("age: "))
    print("name: ",name,"age: ",age )

info()

#HW4 positive and negative

def num():
    num=int(input("enter num= "))
    if num>=0 :
        return "positive" 
    return "negative"
num1=num()

 #HW5 odd and even
def Num():
    num=int(input("enter num= "))
    if num%2==0 :
        return "even" 
    return "odd"
numb= Num()   


#HW 6 dicount 20%

def dis():
    price=float(input("enter the price= "))
    price=price*.80
    return price 
disc=dis()

    
