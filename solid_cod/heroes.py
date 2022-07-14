from weapon import Web, Laser


class SuperHero:

    def __init__(self, name: str):
        self.name = name

    def find(self, place):
        place.get_antagonist()

    def attack(self):
        return 'Kick'

    def ultimate(self):
        return 'Bum'


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
