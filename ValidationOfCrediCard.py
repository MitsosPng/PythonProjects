def credit_check():
    second_sum=0
    first_sum=0
    list=[]
    number=input("Give me a credit card number: ")
    sum=0
    first_digits= number[-1::-2]
    second_digits=number[-2::-2]
    for i in second_digits:
        list.append(i)
    print (list)
    for j in list :
        print ("This is: ", j)
        result=0
        x=int(j)
        x=x*2
        if x >9 :
            while x >0:
                temp = x % 10
                result += temp
                x = x//10 
            print ("Result of ",j," = ",result)
            second_sum+=result
        else: 
            print ("Result of ",j," = ",x)
            second_sum+=x
        print("Total Result= ", second_sum)
        print("")
    print ("This is the result of the second digits ",second_sum)
    for i in first_digits:
        first_sum+=int(i)
    print("This is the result of the first digits: ",first_sum)
    summary=first_sum+second_sum
    print("Ths is total Sum",summary)
    summary*=9
    print("Sum times 9 ",summary)
    if (summary) % 10 == 0 :
        print("Valid Number")
    else:
        print("Not Valid Number")

credit_check()
