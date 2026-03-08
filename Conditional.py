age = int(input(f"Enter you age :"))

if age > 18:
    print(f"You can do!")
elif age == 18:
    print(f"OOO you are begin 18 woo you can.")
else:
    print(f"You can't do!")


print(f"________________________Advance --------")
try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")

    elif age < 13:
        print("You are a child.")

    elif 13 <= age < 18:
        print("You are a teenager. Some things are restricted.")

    elif age == 18:
        print("Congratulations! You just became an adult.")

    elif 18 < age < 60:
        print("You are an adult. Full access granted.")

    elif age >= 60:
        print("You are a senior citizen.")

except ValueError:
    print("Invalid input! Please enter a valid number.")
