intro = "Simple Calculater"
x = int(input("Enter x value:- "))
y = int(input("Enter y value :- "))
print(intro)
ope = input("Enter Mathematical operater (+,-,*,//) :- ")

if ope == "+":
    print(x+y)
elif ope == "-":
    print(x-y)
elif ope == "*":
    print(x*y)
elif ope == "//":
    print(x//y)

