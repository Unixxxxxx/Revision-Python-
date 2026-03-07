Mstk1 = "1.int(input())without try/except"
Mstks2 = "2. Confusing =(assignment)with == (comparision):"
Mstks3 = '3.Mutable default argument def f(x=[]):'
Mstks4 = '4.String + int without casting : "Age:" + 25.'
Mstks5 = '5.int(3.9), not4'
Mstks6 = '6.6.6.6.6.6.Variable names that shadow builtins'
print(f"{Mstk1} :---- Crashes if user types letters; always validated input\n")
print(f"{Mstks2} :--- if x = 5 is a Syntax Error\n")
print(f"{Mstks3} : --- The list  persists across calls!)\n")
print(f"{Mstks4} : ---TypeError, Use F-string or str(23)\n")
print(f"{Mstks5} : ---use round() if you need rounding.\n")
print(f"{Mstks6} : ---list =[] breaks the built-in list()\n")
