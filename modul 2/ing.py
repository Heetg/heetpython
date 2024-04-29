#Write a Python program to add 'ing' at the end of a given string (length should be at least 3)........................................

string = input("Enter a string : ")     

if len(string) >= 3:    
    if string.endswith("ing"):      
        new_string = string + "ly"  
    else:
        new_string = string + "ing"    
else:
    new_string = string     

print("Your New String : ",new_string)      