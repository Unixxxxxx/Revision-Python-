print(f"_---------Function start ------")
def greet(name, greeting="Hello BosS!"):
    """
    Greet a person whit a custom message.
    This Triple-quoted string is a docstring -- always write one!
    """
    return f"{greeting},{name}!"
print(greet('mr.Sharma'))
print(greet('sudhanshu',"hii"))
print(greet(greeting= 'Hey', name ='sHarma')) 
print(f"_________________________________________________________________________")
print('\n')



print(f"*args and **kwargs",'\n ***********VARIABLE ARGUMENT**********************')

def total(*numbers):
    return sum(numbers)
print(f"-------collects positional arguments as a TUPLE----------------------*args")
print(total(1, 2, 3))
print(total(10,20,30, 40))
print(f"_______collect keyword arguments as a DICT______________**kwargs")

def create_profile(**info):
    for key,value in info.items():
        print(f'{key} : {value}')
create_profile(name='Mr', age =25, city='patna/bihar')

print(f"_----------------------------------------------------------------\n")
print(f'---------------------------------------- combining all types (order matters!)')
def func(required, *args, default=0, **kwargs):
    pass


print('\n --------------------------------------------------------SCOPE')



x ='global'

def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print(f'Local-------------finds local first',x)
    inner()
    print(f'enclosing-----------------------',x)

outer()
print(f'global-------------------------------------',x)
print(f"global keyword \n - Modify global from inside function(use sparingly!) ")

count = 0
def increment():
    global count
    count += 1

print(f'=---------------------------------------LAMBDA FUNCTION -----Anonymous one-Line ')


seq = lambda x: x**2
print(seq(5))

print(f"lambda with sorted()---sort by custom key ")


student =[
        {'name' :'Mr.Sharma', 'score' : 100},
        {'name' : 'Mr.Roy', 'score' :99 }]
student.sort(key=lambda s: s['score'], reverse=True )
print(student)

print(f'1. sorts the list | key=lambda s: s[\'score\'] → tells Python to sort using the score value | reverse=True → sorts descending --highest score first--')



print(f'----Recurision ------ function calling Themselves-------------------\n')

print(f'Factorial :n! =n n * (n-1 ) * ... * 1')

print("Factorial: n! = n * (n-1) * (n-2) * ... * 1")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 5
result = factorial(num)

print(f"Factorial of {num} is {result}")
