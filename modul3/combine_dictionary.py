#Write a Python program to combine two dictionary adding values for common ..............................


dic1 = {}  
n=int(input("Enter number of dic1 pairs : "))  
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")   
    value1 = input(f"Enter {i+1} Values : ")
    if value1.isdigit():
        value1 = int(value1) 
        dic1[key1] = value1
    else:
        dic1[key1] = value1

dic2 = {}  
n=int(input("Enter number of dict2 pairs : "))  
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    
    value1 = input(f"Enter {i+1} Values : ")
    if value1.isdigit():
        value1 = int(value1)
        dic2[key1] = value1
    else:
        dic2[key1] = value1


combined_dict = {}     


for key, value in dict1.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

for key, value in dict2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

print(dict1)    
print(dict2)    
print("Combined dictionary : ", combined_dict)      