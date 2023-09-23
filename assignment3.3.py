def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

sample_string = input('enter the string:-')

upper, lower = count_upper_lower(sample_string)

print("No. of Upper case characters:", upper)
print("No. of Lower case characters:", lower)
"""
enter the string:-The quick Brow Fox
No. of Upper case characters: 3
No. of Lower case characters: 12



"""
