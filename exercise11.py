
for i in range (1,100):
    check = False    
    for x in range (2, i):
        if i % x == 0:
        
            check = True
            break
    if check == False:
        print(i)

    