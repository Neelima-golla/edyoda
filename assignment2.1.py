size = int(input("enter the size of the list"))
list = []

for i in range(size) :
    print("Enter the Value:")
    a=int (input("enter value of first"))
    b=int(input ("enter value of second"))
    list.append((a,b))
print(list)
for i in range(1,len(list)):
    curtuple=list[i]
    j=i-1
    while curtuple[1]<list[j][1] and j>=0:
        list[j+1]=list[j]
        j-=1
        list[j+1]=curtuple
print(list)
"""
expected output
enter the size of the list4
Enter the Value:    
enter value of first1
enter value of second1
Enter the Value:    
enter value of first1
enter value of second3
Enter the Value:
enter value of first1
enter value of second2
Enter the Value:
enter value of first1
enter value of second4
[(1, 1), (1, 3), (1, 2), (1, 4)]
[(1, 1), (1, 2), (1, 3), (1, 4)]
"""
