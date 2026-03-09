i=40

number = input("Enter a number: ")

if int(number) < i-20:
    print("too small")

elif int(number) < i:
    print("small")

elif int(number) > i+20:
    print("too big")

elif int(number) > i:
    print("big")

else:
    print("Equal")
