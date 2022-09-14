def horizontal_line(width,char):
    str(char)
    for i in range(width):
        print(char, end="")
    print("")

def vertical_line(shift, height, char):
    str(char)
    for j in range(height):
        for l in range(shift):
            print(" ", end="")
        print(char)

def two_vertical_lines(width, height, char):
    str(char)
    for i in range(height):
        print(char, end="")
        for j in range(width-2):
            print(" ",end="")
        print(char)
# ^ The above prints out specific lines and can be called with the function's name along with its arguments


def number_1(width, char):
    vertical_line(width-1, 5, char)
    return 

def number_0(width, char):
    horizontal_line(width, char,)
    two_vertical_lines(width, 3, char)
    horizontal_line(width, char)
    return

def number_2(width, char):
    horizontal_line(width,char)
    vertical_line(width-1,1,char)
    horizontal_line(width,char)
    vertical_line(0,1,char)
    horizontal_line(width,char)
    return

def number_3(width,char):
    horizontal_line(width,char)
    vertical_line(width-1,1,char)
    horizontal_line(width,char)
    vertical_line(width-1,1,char)
    horizontal_line(width,char)
    return

def number_4(width,char):
    two_vertical_lines(width,2,char)
    horizontal_line(width,char)
    vertical_line(width-1,2,char)
    return

def number_5(width,char):
    horizontal_line(width,char)
    vertical_line(0,1,char)
    horizontal_line(width,char)
    vertical_line(width-1,1,char)
    horizontal_line(width,char)
    return

def number_6(width,char):
    horizontal_line(width,char)
    vertical_line(0,1,char)
    horizontal_line(width,char)
    two_vertical_lines(width,1,char)
    horizontal_line(width,char)
    return

def number_7(width,char):
    horizontal_line(width,char)
    vertical_line(width-1,4,char)
    return

def number_8(width,char):
    horizontal_line(width,char)
    two_vertical_lines(width,1,char)
    horizontal_line(width,char)
    two_vertical_lines(width,1,char)
    horizontal_line(width,char)
    return

def number_9(width,char):
    horizontal_line(width,char)
    two_vertical_lines(width,1,char)
    horizontal_line(width,char)
    vertical_line(width-1,2,char)
    return

# The above are functions which can print numbers 1-9 

def print_number(number,width,char):
    if number==0:
        number_0(width,char)
    if number==1:
        number_1(width,char)
    if number==2:
        number_2(width,char)
    if number==3:
        number_3(width,char)
    if number==4:
        number_4(width,char)
    if number==5:
        number_5(width,char)
    if number==6:
        number_6(width,char)
    if number==7:
        number_7(width,char)
    if number==8:
        number_8(width,char)
    if number==9:
        number_9(width,char)

# print_number(0, 5, '*')
# print_number(1, 6, '*')
# print_number(2, 7, '*')
# print_number(3, 8, '*')
# print_number(4, 9, '*')
# print_number(5, 10, '*')
# print_number(6, 11, '*')
# print_number(7, 12, '*')
# print_number(8, 13, '*')
# print_number(9, 14, '*')

def plus(width,char):
    if ((width % 2) == 0):
        for i in range(int((width / 2)-1)):
            print(" ", end="")
        two_vertical_lines(2, 1, char)
        for i in range(int((width / 2)-1)):
            print(" ", end="")
        two_vertical_lines(2, 1, char)

        horizontal_line(width,char)
        for i in range(int((width / 2)-1)):
            print(" ", end="")
        two_vertical_lines(2, 1, char)
        for i in range(int((width / 2)-1)):
            print(" ", end="")
        two_vertical_lines(2, 1, char)

    
    else:
        vertical_line(width-3,2,char)
        horizontal_line(width,char)
        vertical_line(width-3,2,char)  


def minus(width,char):
    horizontal_line(width,char)

def multiply(width, char):
    left = 0
    middle = width - 2
    flip = False
    if width % 2 == 1 :
        for i in range(width) :
            for j in range(left) :
                print(" ", end="")
            print(char, end="")
            for k in range(middle) :
                print(" ", end="")
            if middle > 0 :
                print(char, end="")
            else :
                flip = True
            print()
            if flip == True :
                middle += 2
                left -= 1
            else :
                middle -= 2
                left += 1
    else :
        for i in range(width-1) :
            for j in range(left) :
                print(" ", end="")
            print(char, end="")
            for k in range(middle) :
                print(" ", end="")
            if middle > 0 :
                print(char, end="")
            else :
                print(char, end="")
                flip = True
            print()
            if flip == True :
                middle += 2
                left -= 1
            else :
                middle -= 2
                left += 1


def division(width, char):
    for i in range(width):
        vertical_line(width-i, 1, char)






def check_answer(number1, number2, ans, op):
    if op =="+":
        if number1 + number2 == ans:
            return(True)
        else:
            return(False)
    if op =="-":
        if number1 - number2 == ans:
            return(True)
        else:
            return(False)
    if op =="*":
        if number1 * number2 == ans:
            return(True)
        else:
            return(False)
    if op =="/":
        if number1 / number2 == ans:
            return(True)
        else:
            return(False)