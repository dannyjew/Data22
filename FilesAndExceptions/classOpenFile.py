class ShakeSpeare():
    def __init__(self, file_path):
        self.file = open(file_path)
        print(self.file)

    def print_lines(self):
        for line in self.file:
            print(line.rstrip('\n'))

    def close_file(self):
        self.file.close()

x = ShakeSpeare("orders.txt")

x.print_lines()

x.close_file()
