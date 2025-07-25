# Print the items and type from the given list 
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

# Loop for each element in the list one by one
for item in datalist:
    print(f"{item} is of type {type(item)}")
