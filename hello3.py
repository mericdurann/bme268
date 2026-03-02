x = 20

if x < 10:
    print("Smaller")

if x == 20:
    print("Equal")

if x > 20:
    print("Bigger")

print("Finish")



x = 7

if x < 2:
    print("small")
elif x < 10:
    print("medium")
else:
    print("large")

print("all Done ")


astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)
astr = 'Hello Bob'
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)