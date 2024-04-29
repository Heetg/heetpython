#Write a Python program to get the Factorial number of given number...............

num=int(input("Enter the  number : "))      

fact = 1    


if num<0:    
    
    print("Enter the  integer number.")
else:   
    for i in range(1,num):
        fact = fact * i     
        i += 1
    print(f"{num} The Factorial is : {fact}")   