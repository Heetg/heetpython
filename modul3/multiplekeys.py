#Write a Python program to check multiple keys exists in a dictionary...........................

dic1 = {} 
n=int(input("Enter number of dictionary1 pairs : "))  
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    
    value1 = input(f"Enter {i+1} Values : ")
    dic1[key1] = value1    

check_key = []    
n2 = int(input("Enter number of check keys : "))    


for i in range(n2):
    input_key = input(f"Enter {i+1} keys : ")
    check_key.append(input_key)    

print(dic1)
for key in check_key:
    if key not in dic1:
        print(f"{key} does not exists in a dictionary.")    
    else:
        print(f"{key} exists in a dictionary.")     