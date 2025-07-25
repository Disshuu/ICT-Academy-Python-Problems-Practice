# count the number of even and odd in the given numbers
numbers = (1,2,3,4,5,6,7,8,9)# given tuples are there

# counter for even and odd
even_count = 0
odd_count = 0

# loop for each number passing
for nums in numbers:
    if nums % 2 == 0:
        even_count +=1 # the number is even
    else:
        odd_count +=1 # the number is odd
        
print("Numbers of even numbers:",even_count)
print("Numbers of odd numbers:",odd_count)            
        