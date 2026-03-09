hours = input("Hours you work: ")
rate = input("Rate: ")

def payment(hours, rate):
    if int(hours) <= 40:
        money = int (hours) * float(rate)
    elif int(hours) > 40:
        money = (40 * float(rate)) + ((int (hours) - 40) * float(rate) * 1.5)
    return money

print("You made", payment(hours, rate), "dollars")  