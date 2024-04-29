
#Write a Python function to check whether a number is in a given range

def is_in_range(num, start, end):    
    if num >= start and num <= end:
        print(f"The number {num} is in the given range [{start}, {end}].")
    else:
        print(f"The number {num} is not in the given range [{start}, {end}].")

num= int(input("Enter a number : "))    
range_start = int(input("Enter the start of the range : "))
range_end = int(input("Enter the end of the range : "))

is_in_range(num, range_start, range_end)    
