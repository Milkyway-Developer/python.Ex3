# binary = []
# c = 0
# d = 0
# tedad_adad_binary=int(input("tedad adad binary ra vard kon:"))
# for a in range(tedad_adad_binary):
#     number = int(input("Enter the number :"))
# binary.append(number)
# while True:
#     for i in binary:
#         if i ==0 or i==1:
#           b = ((2**c)*i)
#           c += 1
#           d += b
#     print(d)
# binary to num #

#Modified code below ^ v ^

binary = []
desimal = 0
tedad_adad_binary = int(input("tedad adad binary ra vard kon:"))
for a in range(tedad_adad_binary):
    number = int(input("Enter the number 0 or 1:"))
    if number not in [0, 1]:
        print("just enter 0 or 1")
        exit()                                #if number not in [0, 1] This command stops the entire program immediately.
    binary.append(number)
c = len(binary) - 1
for i in binary:
    desimal += (2**c) * i
    c -= 1
print(f"meghdar adadi : {desimal}")
