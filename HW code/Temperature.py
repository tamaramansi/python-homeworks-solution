def Fah(C):
    F=1.8*C +32
    return F

def Cel(f):
    c=(f-32)/1.8
    return c

def weathcon (temp):
    if temp >15:    
        if temp>30:
          return("so hot")
        if temp>=16 and temp<25:
         return "Moderate"
        return "close to hot"
    if temp<=15:
       if temp>5 and temp<15:
           return "cold"
       if temp >0 and temp<=5:
           return "freez"
       return "freezing"
