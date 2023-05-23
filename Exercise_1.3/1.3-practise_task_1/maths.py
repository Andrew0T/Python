# basic python script add and minus program
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
operator = input("Enter + or - ")

if operator == "+":
  print("result: ", str(a + b))

elif operator == "-":
  print("result: ", str(a - b))

else:
  print("This operator not available!")