for i in range( 1,7):
    print('\n',f"Range | Print number from 1-7 | starts from 1 and stops before 6  | ",(i))
print("\n", f"--------------------------------------------------------------------------------------")
for x in range(1,11):
    if x % 2 ==0:
        print(f"Print only even numbers from 1-11 | ", (x))
print("----------------------------------------------------------------------------------")

num = 1 
while num <= 5:
    print(num)
    num += 1

print(f"____________________________________________________________________________")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
print("____________________________________________________________________________________\n")

secret = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct Guess!")
        break

    elif guess < secret:
        print("Too small!")

    else:
        print("Too large!")
        


print(f"----------------------------------Password Attempts System---------\n")

correct_password = "LutheR"

for attempt in range(3):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")

else:
    print("Account Locked")
