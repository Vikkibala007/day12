a=int(input("enter the first number "))
b=int(input("enter the second number "))
for i in range(a,b):
    if i > 1:
        for j in range (2,i):
            if(i%j)==0:
                break
        else :
            print(i)
           
