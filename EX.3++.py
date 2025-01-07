our_numbers = []
E = 0
O = 0
m = int(input("how many numbers you want to enter:"))
for i in range(m):
    number_input = int(input("Enter the list of your numbers:"))
    our_numbers.append(number_input)
for a in our_numbers:
    if a%2==0:
        E+=1
    else:
        O+=1
print(f"there is {E} even number and {O} odd number  ")