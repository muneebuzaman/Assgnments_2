import random
random_numbers=tuple(random.randint(1,10) for _ in range (5))
number_to_check=7
found=False
for num in random_numbers:
    if num==number_to_check:
        found =True
        break
if found:
    print(f'The number {number_to_check} exists in the tuple.')
else:
    print(f'The number {number_to_check} does not exists in the tuple.')
print('Generated tuple:',random_numbers)

