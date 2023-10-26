#Functions
'''def add_num(a,b,c):
    sum = a+b+c
    print('the sum is:', sum)

print(add_num(1,5,7))

def multi(x):
    return x*5


def my_func(fname):
    print(fname + " John")

my_func('george')


#arbitrary arguments: unknown number of parameters or arguments
def addnum(*a):
    sum = 0
    for num in a:
        sum += num
    return sum
print(addnum (6,9))


def mf(*kids):
    print('the youngest child is'+ kids[2])

    mf('Prince', 'Jay', 'Crownz')

def myf(**kid):
    print('the youngest child is ' + kid['lname'])
kid(fname = chima, lname = nest)


def intro(**data):
    print('\nData type:', type(data))
    for key, value in data.items():
        print(f'{key} is {value}')

intro(firstname = 'John', lastname = 'Jake', email = 'jjake@gmail.com', country = 'Naija', age = '23')


#lambda expression-> single use function
x = lambda a: a + 10
print (x(5))'''


#takes in n and returns the square of n
def square(n):
    return n**2