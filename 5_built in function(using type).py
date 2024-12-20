def type_checker(input_data):
    datatype=type(input_data)
    return datatype
a=type_checker(44)
b=type_checker('python')
c=type_checker(4.4)
d=type_checker([1,2,3])
e=type_checker({1:'apple',2:'banana',3:'grapes'})
f=type_checker((1,3,'mango'))

print(a,'\n',b,'\n',c,'\n',d,'\n',e,'\n',f)

