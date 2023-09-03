def check_age():
    i = 0
    while True: 
        age = int(input("Enter age: "))
        i += 1
        if int(age) >= 1 and int(age) <= 100:
            print('Your age is ' + str(age))
            print('Number of attempts = ' +str(i))
check_age()