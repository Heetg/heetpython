
#Write a Python program to create a tuple with different data types.

tuple1 = ("tuple", True, 4, 5)   
print(tuple1)   #display tuple

tuple1 = []     
n = int(input("Enter a number of element : "))  

for i in range(n):
    input_element = input("Enter a element : ")
    if input_element.isdigit():
        input_element = int(input_element)     
    tuple1.append(input_element)    

print(tuple(tuple1))    
