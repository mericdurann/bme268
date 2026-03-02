print("Enter the hours you worked: ")

hours = input()

print("Enter Rate:")

rate = input()

if int(hours) <= 40:
    money = int (hours) * int(rate)
elif int(hours) > 40:
    money = (int (hours) * int(rate)) + ((int (hours) - 40) * int(rate) * 1.5)

print("You made", money, "dollars")


