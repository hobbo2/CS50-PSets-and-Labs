def main():
    height = get_height()
    # iterate over the #'s using a loop
    for i in range(height):
        # spaces on left
        spaces = height - (i + 1)
        height_left = (height + 1 - (height - i))
        height_right = (height + 1 - (height - i))
        print(" "*spaces+"#"*height_left+"  "+"#"*height_right)


# check height is integer above 0 and below 9
def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n <= 8 and n > 0:
                return n
        except ValueError:
            print()


# call the main function
main()

