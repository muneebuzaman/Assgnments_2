def count_character(input_sting):
    char_count={}
    for char in input_sting:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count
input_string='hellow world'
result=count_character(input_string)
for char,count in result.items():
    print(f"'{char}':{count}")