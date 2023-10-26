'''#First function
def addnumsum(a,b):
    sum = a + b
    return 2*sum
#Using the function
print(addnumsum(4,3))'''

#Second function
def dict(**data):
    for key, value in data.items():
        print(f'{key} is {value}')
#Using the function
dict(first_name = 'Tuco', last_name = 'Saalamanca', email = 'tucosala@bb.com', phone_number = '0222622')


'''#Third function
def vals(*fruits):
        print('the second fruit is ' + fruits[1], '\nthe third fruit is ' + fruits[2], '\nthe fifth fruit is ' + fruits[4])
#Using the function
vals('orange', 'banana', 'apple', 'pear', 'grape')'''
    
