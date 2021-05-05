def  fibonacci(up_to_what_number):
    num1=0
    num2=1
    print(num1)
    print(num2)
    i=0
    while(i<up_to_what_number):
        num3=num1+num2
        print(num3)
        num1=num2
        num2=num3
        i+=1
up_to_what_number=int(input("Please enter a number"))
fibonacci(up_to_what_number)





