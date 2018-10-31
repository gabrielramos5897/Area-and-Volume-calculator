import sys
def main():
    eq = float(input("What is the Equation you are looking for?\nArea = 1\nVolume = 2\n"))
    if eq == 1:
        def fname():
            length = float(input("What is the Length?"))
            width = float(input("What is the Width?"))
            return length * width
        print(fname())
    elif eq == 2:
        def volume():
            length = float(input("What is the Length?"))
            width = float(input("What is the Width?"))
            vol = float(input("What is the Height?"))
            return length * width * vol
        print(volume())
    else:
        print("The input was invalid")

    restart = float(input("Would you like to start over?"))

    if restart == 1:
        main()

    elif restart == 2:
        sys.exit()
main()
