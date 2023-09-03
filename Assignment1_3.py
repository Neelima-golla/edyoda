numbers=(1,2,3,4,5,6,7)

even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
print (f"no of even no are {even} \nno of odd  no are {odd} ")
