try:
    # file = open("order.txt")
    x = 4/0
except FileNotFoundError as errmsg:
    print("There has been an error! Panic!")
    print(errmsg)
except ZeroDivisionError as errmsg:
    print("You cannot divide by 0 you fool!")
    print(errmsg)
    raise






