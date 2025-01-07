import math

choose = input("choose from the log , jazr , 2nd degree equation or power : ")
if choose == "log":
    a = int(input("Enter The number you want to take logarithm from :"))
    b = int(input("Enter the base of the logarithm: "))
    print((math.log(a, b)))
elif choose == "jazr":
    c = int(input("Enter the num you want to take jazr from: "))
    print(math.sqrt(c))
elif choose == "2nd degree equation":
    A = int(input("Enter the variable A of the equation: "))
    B = int(input("Enter the variable B of the equation: "))
    C = int(input("Enter the variable C of the equation: "))
    delta = math.pow(B, 2) - 4 * A * C
    if delta == 0:
        x = -B / 2 * A
        print(f"we have one answer:{x}")
    elif delta > 0:
        X1 = (-B + math.sqrt(delta)) / 2 * A
        X2 = (-B - math.sqrt(delta)) / 2 * A
        print(f"we have two answers:x1:{X1}and X2:{X2}")
    elif delta < 0:
        print("This equation dosent have any answer")
elif choose == "power":
    base = int(input("Enter the base num :"))
    Power = int(input("Enter your power :"))
    print(math.pow(base, Power))

#ب.ب.ک عملیات ریاضی پیچیده مثل لگاریتم را انجام دهد.