# Divisible by 7 and multiple of 5 

result = []

for i in range(1500,2701):
    if i % 7 == 0 and i % 5 == 0:
        result.append(i)# inclusive(python go up but not in the end point)
        
# print("Number divisible by 7 and multiple by 5 between 1500 to 2701:")
# print(result)
print(",".join(str(num)for num in result))        