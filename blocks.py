#for i in range (1,13):
 #   print("No. {} squared is {} and cubed is {:4}".format(i,i**2,i**3))

name = input("what's your name: ")
age = int(input("How are old are you, {0} ".format(name)))

if age >= 18:
    print("You can vote")
    print("Please put an x in the box")
else:
    print("Please come back in {0} years".format(18-age))

if age < 18:
    print("Please come back in {0} years".format(18-age))
else:
    print("You can vote")
    print("Please put an x in the box")
