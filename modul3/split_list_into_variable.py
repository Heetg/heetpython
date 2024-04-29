
#Write a Python program to split a list into different variables.

list1 = []
n = int(input("Enter number of element : "))    #get value from user

if n!=0:
    for i in range(n):
        list1_input = input("Enter a number : ")    #get value from user
        list1.append(list1_input)   #add element in a list

    for j in range(n):
        print(f"var{j+1} = {list1[i]}")     #display list into different variable

else:
    print("Enter valid number of element.")

