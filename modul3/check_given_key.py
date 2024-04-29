# Python3 Program to check whether a given key already exists in a dictionary. 

def checkKey(dic, key): 
n=int(input("Enter number of dict1 pairs : "))
	if key in n.keys(): 
		print("Present, ", end =" ") 
		print("value =", n[key]) 
	else: 
		print("Not present") 
		 
dic = {'a': 100, 'b':200, 'c':300} 
key = 'b'
checkKey(dic, key) 

