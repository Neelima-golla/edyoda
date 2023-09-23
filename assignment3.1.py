lst_for_sum=[]
no_of_items=int(input("enter the no of items to be inserted in list "))
for i in range(no_of_items):
    number=int(input(f'enter the {i+1} value '))
    lst_for_sum.append(number)
print(lst_for_sum)
def sum_of_list(lst):
    sum=0
    for i in lst:
        sum+=i
    print(f'the sum of list is {sum}')

sum_of_list(lst_for_sum)
"""
expected output 
enter the no of items to be inserted in list 5
enter the 1 value 1
enter the 2 value 2
enter the 3 value 3
enter the 4 value 4
enter the 5 value 5
[1, 2, 3, 4, 5]
the sum of list is 15

"""
