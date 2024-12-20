numbers=(1,2,3,4,5)
total_sum=0
largest_number=numbers[0]
smallest_number=numbers[0]
for num in numbers:
    total_sum=total_sum+num
    if num>largest_number:
        largest_number=num
    if num<smallest_number:
        smallest_num=num
print(f'The sum of all numbers is {total_sum}')
print(f'The largest number is:{largest_number}')
print(f'The smallest number is:{smallest_number}')