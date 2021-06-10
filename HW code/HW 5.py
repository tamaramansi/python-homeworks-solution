#HW 1 prime numbers between (20-70)

for x in range(20,71):
    if x%2!=0 and x%3 !=0 and x%5 !=0 and x%7!=0 :
        print(x)
        
#HW 2 greatest common division 

num1=int(input("input num1 = "))
num2=int(input("input num2 = "))
for i in range (1,num2+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("GCD= ",gcd)


#hw3 two shape program
for i in range(5,0,-1):
        for j in range(1,i+1):
            print("* ",end="")
        print("\r")  
        
k = 2*5 - 2 # number of spaces 
for i in range(0,5):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
 