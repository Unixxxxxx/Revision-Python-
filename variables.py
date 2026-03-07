#A variabels is a name container that stores a value in memory. Think of it labelled box.

print(f"**********************VARIABLE **************  aSSIGNMENT *****************")
name  = 'Alice'
age  = 25
height = 5.9
is_student = True
result = None 

# print function working (simple)
print(name,age,height,is_student,result)

# using f-string (for clear and professional) 
print(f'{name} {age} {height} {is_student} {result}')

print(f" *****************Use format()      |   Function for print ")
print("{} {} {} {} {}".format(name,age,height,is_student,result))

# f""   | Strings 
print(f"{name}, {age}, {height}, {is_student}, {result}")


print(f'***************************************Multile Assignment *********************************************')
x = y = z = 0
a,b,c = 1,2,3

print(x,y,z)
print(a, b, c)

# swipe without a temp variable *********A temporary variables is a help veriable used to store value from short time while performing an operation.
a,b = b,a 
print(a,b)
print(b,a)

print(f"*************************   |   Check type at runtime   |")

print(type(name))
print(type(is_student))

print(f"*********************************Complex Number__________^_^")
dif = "A complex number in Python is a number that contains a real part and an imaginary part, written as a + bj."
part1 = "Real_Part" 
part2 = "Imaginary_Part" 
print(f"A complex number ia a number that has two part:\n{part1}\n{part2}")
print(f"short Difination\n{dif}")
print(f"******************EXAMPLE****************")
x = complex(1,2)
print(x)
c = 3+4j
print(c.real)
print(c.imag)



print(f"**********************INPUT and OutPut ********************")
# output print
print('Name:'  "Alice")
me = 'alpha' 
age = 25

print(f"Name:{me}\nage:{age}")

print(f"***INPUT- Always return TRUE ********")

#name = input('Enter Your Name :\n ')
#email = input('Enter Your Mail:\n')

#print(f"This is my name {name} and my email is {email}")


print(f"**********************Type Casting__________^^__^^ ")
m=int('2')
n= int(1.9)
print (type(f"{m}"))
print(type(f"{n}"))


print(f"***************************************TYPE CASTING******************\n")
topic="Truncats\n"
diff  =  "Truncats often means removing the decimal part of a number"
print(f"Topic{topic}: \nDiff: {diff}\n__^^__\n")
import math
b = 5.9
print(math.trunc(b))
print(round(b))
Trun = "Remove Decimell"
Round = "go to the nearest Number"
math.ceil = "Rounds up to nearest integer"
math.floor = 'Rounds down to nearest integer'
math.trunc = 'Removes decimal part'
print(f"Truncat:{Trun}\nRound:{Round}\n math.ceil : {math.ceil} \n math.floor: {math.floor} \n math.trunc : {math.trunc}")

print(f"*****************************self Input with validation for **Indestry standard**___^")
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("X Invalid : Please enter a whole Number")
age = get_integer("enter your age:")
print(f"your age is : {age}")

print(f"\nExplanation : \n")
get, inte, except_valueError, while_True = [
    "asks the user for input.",
    "tries to convert the input to an integer.",
    "If the user enters something like 'abc' → ValueError occurs.",
    "catches the error and prints a message.",
]
print(f"get : {get},\n inte : {inte},\n except : {except_valueError},\n while : {while_True}")


print(f"\n Custom sepration *********************************")
print('2026', '02', '12', sep='-')
print(f"\n Custom end(defaultin new line)")
print(f"Loading", end="..........")
print(f"print to file use for logging....")
import sys
print("Error Occured", file= sys.stderr)

print(f"******************************Flush Buffer immediately(Important in real time app")
print("Processing.......",flush=True)


print(f"*********f-sting----Professional way******\n")

Product = 'Alice'
score = 95.567
price = 1234567.89
# Basic
print(f"Product: {Product}!")
#Decimel formatting 
print(f"score:{score:.2f}")
#Thousand Seprator
print(f"price: {price: .2f}")
#padding and alignement
print(f"{'left': <10}|")
print(f"{'Right': >10}|")
print(f"{'center' : ^10}|")


print(f"*********************None Type**************None is Not Zero, Not False, Not empty string")
print(None == 0)
print(None == False)
print(None is None)  #True | correct way to check 

print(f"************Common real-world use : Function with no return**********")

def do_somthing():
    s = 4+2
    return  s
result = do_somthing()
print(result)

print(f"""\n*********Explanation ******\n
....do_somthing() → function runs.\n
....s = 4 + 2 → value becomes 6.\n
....return s → sends 6 back.\n
....result = do_somthing() → stores 6 in result.\n
....print(result) → prints 6.\n""")
