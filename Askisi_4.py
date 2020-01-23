import math
def f(x, y):
    a = math.floor(math.log10(y))
    return int(x*10**(1+a)+y)

def string_to_number():
    string=input('Give me a string: ')
    list=[]
    count=0
    number=0
    for i in string:
        count+=1
        list.append(ord(i))
    for i in range(count):
        number=f(number,list[i]) 
   
    print("The list of the string in ASCII is",list)
    print("The Number Is: ",number) 
    
    
    if number > 1: 
      
   # Iterate from 2 to n / 2  
        for i in range(2, number//2): 
         
       # If number is divisible by any number between  
       # 2 and n / 2, it is not prime  
            if (number % i) == 0: 
                print(number, "is not a prime number") 
                break
        else: 
            print(number, "is a prime number") 
    else: 
        print(number, "is not a prime number") 

string_to_number()
