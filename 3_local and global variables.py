#phase 1
# this code will show error because it takes counter as a local variable in function which is not initialized

# counter=0
# def increment_counter():
#     counter=counter+1
#     print(f'inside function,counter={counter}')
# increment_counter()
# increment_counter()
# increment_counter()
# print(f'outside function,counter={counter}')

#phase 2
#modified using global keyword
counter=0
def increment_counter():
    global counter
    counter=counter+1
    print(f'inside function,counter={counter}')
increment_counter()
increment_counter()
increment_counter()
print(f'outside function,counter={counter}')

