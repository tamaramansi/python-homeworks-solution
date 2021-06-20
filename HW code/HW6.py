#HW1 Grade 
def grade(mark):
    if(mark<50):
        return"F"
    if (mark>=50 and mark <65):
        return"D"
    if (mark>=65 and mark <80):
        return"C"
    if (mark>=80 and mark <90):
        return"B"
    if (mark>=90):
        return"A"
Grade= grade(87)
Grade1= grade(60)
Grade2= grade(95)
Grade3= grade(40)

#HW2 SWAP

def swap():
    n1=int(input("n1= "))
    n2= int(input("n2= "))
    print("before swaping: n1= ",n1,", n2= ",n2)
    print("after swaping: n1= ",n2,", n2= ",n1)
swap()

#HW3 Draw rectangular

def rectangular ():
    width =int(input("W = "))
    Height =int(input("H = "))
    fill = "*"
    x=1
    y=1
    z=1
    while x<=width:
     print(fill,end="")
     x+=1
    while y<=Height:
       print("\n")
       y+=1
    while z<=width:
      print(fill,end="")
      z+=1
rectangular()


#HW4 CalcShapeArea 
def calcShapeArea (name_of_the_shape): 
    if (name_of_the_shape == "Triangle"):
        height=int(input("TriHeight= "))
        base =int(input("TriBase= "))
        area=0.5*base*height  
        return area
    if (name_of_the_shape =="Rectangular"):
        length=int(input("RecLength= "))
        Width=int(input("RecWidth= "))
        area= length*Width
        return area
    if(name_of_the_shape =="Square"):
        dim=int(input("SquDimention= "))
        area= dim**2
        return area 
    if (name_of_the_shape == "Circle") :
        radius=int(input("radius= "))
        area= 3.14159 *(radius**2)
        return area 
areaOfCircle = calcShapeArea("Circle")
areaOfTriangle= calcShapeArea("Triangle")
areaOfRectangular= calcShapeArea("Rectangular")
areaOfSquare= calcShapeArea("Square")






