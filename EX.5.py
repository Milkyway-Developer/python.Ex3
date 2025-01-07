# https://www.aparat.com/v/c95e2xj
choose = str(input( "a or b :"))
if choose == "a":
   number_to_binary = int(input("enter the number: "))
   a = bin(number_to_binary)
   print(a)
elif choose == "b":
    number_to_binary = str(input("enter the number: "))
    b = int(number_to_binary,2)
    print(b)

#هم عدد به باینری هم باینری به عدد ^^

#اینا کار نمیکنند:)
# number = int(input("Enter the number :"))
# lst_binary =[]
# while number >0:
#     a = number%2
#     lst_binary.append(a)
#     number = number//2
#     for i in lst_binary:
#      print(i,end="")
# num to  binary #

