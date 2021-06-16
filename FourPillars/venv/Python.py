from Snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

Ola = Python()
Aaron = Python()
Aaron.eyes = False
print(Aaron.eyes)
print(Ola.large)