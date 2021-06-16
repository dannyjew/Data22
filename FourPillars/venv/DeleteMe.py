class friendly():
    def __init__(self, name = "dwarf 1", health = "100"):
        self.name = name
        self.health = health
        self.attack_player = False


class dwarf(friendly):
    def __init__(self, name, health):
        super().__init__(name, health)


gimli = dwarf("gimli", 50)
print(gimli.name)
print(gimli.health)