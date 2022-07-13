from weapon import Gun, Web, Laser


class SuperHero(Gun):

    def __init__(self, name: str):
        self.name = name

    def find(self, place):
        place.get_antagonist()

    def attack(self):
        self.fire_from_a_pistol()

    def ultimate(self):
        self.fire_from_a_gun()


class Superman(SuperHero, Laser):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent')

    def attack(self):
        self.powerful_blow()

    def ultimate(self):
        self.incinerate_with_lasers()


class SpiderMan(SuperHero, Web):

    def __init__(self):
        super(SpiderMan, self).__init__('Spider-man')

    def attack(self):
        self.web_gun()

    def ultimate(self):
        self.web_bomb()
