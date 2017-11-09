while True:
  num = int(input("Enter odd number"))

  if (num % 2 == 0):

    print("Your number is even number")

while num % 2 != 0:
   for i in range(num, num + 2):
     for a in range(i, i + 2):
       print(a, end="")
       print("")