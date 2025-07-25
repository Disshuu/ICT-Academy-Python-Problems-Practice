# print the diamond with upper part increasing and lower part decreasing
for i in range(1,6): # outer loop control the rows in the stars
    for j in range(i): # inner loop control how many stars in each rows
        print("*", end=" ")
    print( ) # new line after each row
# Lower part of the diamond (decreasing)
for i in range(4,0,-1):
    for j in range(i): 
        print("*", end=" ")
    print( )   #newline     