def open_print_file(file):
    try:
        with open(file, "r") as opened_file:
            for line in opened_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("File cannot be found in the directory")
        raise
    finally:
        print("\nExecution complete")


open_print_file("orders.txt")