# prompt user for valid input
while True:
    try:
        change = float(input("Change owed: "))
        if change > 0:
            break
    except:
        ValueError


# declare coins
coins = 0
# multiply change by 100 so work in whole numbers
change = change * 100

# work out amount of quarters
# double // returns int and / returns float
coins += change // 25
change %= 25

coins += change // 10
change %= 10

coins += change // 5
change %= 5

coins += change // 1


print(int(coins))