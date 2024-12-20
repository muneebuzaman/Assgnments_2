import random
def generate_random_numbers(n,a,b):
    random_numbers=[]
    for i in range(n):
        num=random.randint(a,b)
        random_numbers.append(num)
    return random_numbers
random_numbers=generate_random_numbers(5,1,20)
print(f'Generated random numbers:{random_numbers}')
