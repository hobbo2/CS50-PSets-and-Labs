# TODO

def main():
    height = get_height()
    for i in range(height):
        spaces = height - (i + 1)
        print(" "*spaces+"#"*(height + 1 - (height - i)))


def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n <= 8 and n > 0:
                return n
        except ValueError:
            print()

#call the main function
main()

