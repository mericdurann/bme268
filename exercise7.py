
#example1

i=10

while i>0:
    print(i)
    i = i-1

print("test done!")

#example2 

while True:
    x = input("Enter a something: ")
    if x == "done":
        break
    else:
        print("enter again")

print ("done!")

#example3

while True:
    line = input('> ')
    if line[0] == '#' : 
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

