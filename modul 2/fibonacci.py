#Write a Python program to get the Fibonacci series of given range..............




num=int(input("Enter  number of terms : "))   

num1 = 0     

num2 = 1

for i in range(1,num):
    if i<=1:    
        num3 = i
    else:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    print(num3)     