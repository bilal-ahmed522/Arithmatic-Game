import Myfunctions
import random




problems = 0
digi = 0
char = ""
correctCount = 0
count = 0

addCount = 0
addCorrect = 0
addPercent = 0

subCount = 0
subCorrect = 0
SubPercent = 0

multiCount = 0
multiCorrect = 0
multiPercent = 0

divCount = 0
divCorrect = 0
divPercent = 0

while True:
    problems = int(input("enter number of problems: "))
    if problems <= 0:
        print("invalid")
    else:
        break

while True:
    digi = int(input("Width of digits (5 - 10): "))
    if digi < 5 or digi > 10:
        print("invalid width")
    else:
        break

drillMode = input("Drill mode? (Y or N) ")


while True:
    char = str(input("enter charachter: "))
    if len(char) == 1:
        break
    print("too many characters")
print()
print("Here we go!")
print()



if drillMode == "yes":
    for i in range(problems):
        num1 = 0
        num2 = 0
        count = 0
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        ranOp = random.randint(1,4)

        while num2 == 0:
            num2 = random.randint(0,9)
        while num1 % num2 > 0:
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
            while num2 == 0:
                num2 = random.randint(0,9)



        print("what is.....")
        print()
        Myfunctions.print_number(num1, digi, char)
        print()

        if ranOp == 1:
            op = "-"
            Myfunctions.minus(digi,char)
            subCount += 1 
            print()
        elif ranOp == 2:
            op = "+"
            Myfunctions.plus(digi, char)
            addCount += 1
            print()
        elif ranOp == 3:
            op = "*"
            Myfunctions.multiply(digi,char)
            multiCount += 1
            print()
        elif ranOp == 4:
            op ="/"
            Myfunctions.division(digi,char)
            divCount += 1
            print()

        Myfunctions.print_number(num2, digi, char)
        print()

        while True:
            answer = int(input("= "))

                    
            if Myfunctions.check_answer(num1, num2, answer, op):
                count += 1
                print("Correct")
                if count == 1:
                    correctCount += 1
                break
            else:
                print("Incorrect")
                count += 1
else:
    for i in range(problems):
        num1 = 0
        num2 = 0
        count = 0
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        ranOp = random.randint(1,4)

        while num2 == 0:
            num2 = random.randint(0,9)
        while num1 % num2 > 0:
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
            while num2 == 0:
                num2 = random.randint(0,9)



        print("what is.....")
        print()
        Myfunctions.print_number(num1, digi, char)
        print()

        if ranOp == 1:
            op = "-"
            Myfunctions.minus(digi,char)
            subCount += 1 
            print()
        elif ranOp == 2:
            op = "+"
            Myfunctions.plus(digi, char)
            addCount += 1
            print()
        elif ranOp == 3:
            op = "*"
            Myfunctions.multiply(digi,char)
            multiCount += 1
            print()
        elif ranOp == 4:
            op ="/"
            Myfunctions.division(digi,char)
            divCount += 1
            print()

        Myfunctions.print_number(num2, digi, char)
        print()
        answer = int(input("= "))

        if Myfunctions.check_answer(num1, num2, answer, op):
            count += 1
            print("Correct")
            if count == 1:
                correctCount += 1
                if op == "+":
                    addCorrect += 1
                elif op == "-":
                    subCorrect += 1
                elif op == "*":
                    multiCorrect += 1
                else:
                    divCorrect += 1
        else:
            print("Incorrect")
            count += 1 
    print()
    print("you got", correctCount, "out of", problems, "correct!" )
    print()
    if addCount >= 1:
        print()
        print("Total addition problems presented:", addCount)
        addPercent = ((addCorrect / addCount) * 100)
         # format(addPercent, ".2f")
        print("Correct addition problems:", addCorrect, end="")
        print(" (",addPercent,"%)", sep="")
        print()
    else:
        print()
        print("No addition problems presented")
        print()
    if subCount >= 1:
        print()
        print("Total subtraction  problems presented:", subCount)
        SubPercent = ((subCorrect / subCount) * 100)
         # format(addPercent, ".2f")
        print("Correct subtraction problems:", subCorrect, end="")
        print(" (",SubPercent,"%)", sep="")
        print()
    else:
        print()
        print("No subtraction problems presented")
        print()
    if multiCount >= 1:
        print()
        print("Total multiplication problems presented:", multiCount)
        multiPercent = ((multiCorrect / multiCount) * 100)
         # format(addPercent, ".2f")
        print("Correct multiplication problems:", multiCorrect, end="")
        print(" (",multiPercent,"%)", sep="")
        print()
    else:
        print()
        print("No multiplication problems presented")
        print()
    if divCount >= 1:
        print()
        print("Total division problems presented:", divCount)
        divPercent = ((divCorrect / divCount) * 100)
         # format(addPercent, ".2f")
        print("Correct division problems:", divCorrect, end="")
        print(" (",divPercent,"%)", sep="")
        print()
    else:
        print()
        print("No division problems presented")
        print()