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
