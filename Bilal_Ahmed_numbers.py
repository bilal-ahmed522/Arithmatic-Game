def is_even(posInt):
    if ((posInt % 2) == 0):
        return(True)
    else:
        return(False)

def is_odd(posInt):
    if ((posInt % 2) == 0):
        return(False)
    else:
        return(True)

def is_prime(posInt):
    num_factors = 0
    k = 2
    if posInt == 1:
        return(False)
    while k < posInt:
        if posInt % k == 0:
            num_factors += 1
        k += 1
    if num_factors == 0:
        return(True)
    else:
        return(False)

def is_perfect(posInt):
    num_factor = 0
    for i in range(1, posInt):
        if(posInt % i == 0):
            num_factor = num_factor + i
    if (num_factor == posInt):
        return(True)
    else:
        return(False)

def is_abundant(posInt):
    num_factor=1
    for i in range(2,posInt):
        if (posInt % i==0):
            num_factor=num_factor+i
    if(num_factor>posInt):
        return(True)
    else:
        return(False)

def validStart(startingNum):
    while True:
        startingNum = int(input("Enter starting num: "))
        if startingNum <= 0:
            print("Invalid")
        else:
            return(startingNum)

def validEnding(startingNum, endingNum):
    while True:
        endingNum = int(input("Enter ending num: "))
        if endingNum <= 0 or endingNum < startingNum:
            print("Invalid")
        else:
            return(endingNum)
       


choice = 0


while True:
    print("Main Menu")
    print()
    print("1 - Find all prime numbers within a given range")
    print("2 - Find all perfect numbers within a given range")
    print("3 - Find all abundant numbers within a given range")
    print("4 - Chart all even, odd, prime, perfect and abundant numbers within a given range")
    print("5 - Quit")
    print()
    choice = int(input("choice: "))


    if choice > 5:
        print("I don't understand that...")
    if choice == 5:
        break
    startingNum = 0
    endingNum = 0

    if choice == 1:
        
        startingNum = validStart(startingNum)
        endingNum = validEnding(startingNum, endingNum)

        print("All prime numbers between", startingNum, "and", endingNum)
        print("###############")
        i = startingNum
        while i <= endingNum:
            if is_prime(i) == True:
                print(i)
            i += 1
        print("###############")
    if choice == 2:
        startingNum = validStart(startingNum)

        endingNum = validEnding(startingNum, endingNum) 
        print("All perfect numbers between", startingNum, "and", endingNum)
        print("###############")
        i = startingNum
        while i <= endingNum:
            if is_perfect(i) == True:
                print(i)
            i += 1
        print("###############")

    if choice == 3:
        startingNum = validStart(startingNum)
        endingNum = validEnding(startingNum, endingNum)

        print("All abundant numbers between", startingNum, "and", endingNum)
        print("###############")
        i = startingNum
        while i <= endingNum:
            if is_abundant(i) == True:
                print(i)
            i += 1
        print("###############")
    if choice == 4:
        startingNum = validStart(startingNum)
        endingNum = validEnding(startingNum, endingNum)

        print("Number    Even      Odd      Prime      Perfect        Abundant")
        for i in range(startingNum, endingNum+1):
            print(i, end="")
            iL = str(i)
            iL = len(iL)
            for j in range(10-iL):
                print(" ", end="")
            if (is_even(i)== True):
                print("X",end="")
            else:
                print(" ",end="")
            if (is_odd(i)==True):
                print("          X", end="")
            else:
                print("           ",end="")
            if (is_prime(i)== True):
                print("         X", end="")
            else:
                print("          ",end="")
            if (is_perfect(i)==True):
                print("         X", end="")
            else:
                print("          ", end="")
            if (is_abundant(i)==True):
                print("               X", end="")
            else:
                print("                ", end="")
            print()


        
