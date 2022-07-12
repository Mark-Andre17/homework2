from abc import abstractmethod


class SuperHero:

    def __init__(self, name: str):
        self.name = name

    def find(self, place):
        place.get_antagonist()

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def ultimate(self):
        pass


class Superman(SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent')

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')

    def attack(self):
        print('Kick')

    def ultimate(self):
        self.incinerate_with_lasers()


class SpiderMan(SuperHero):

    def __init__(self):
        super(SpiderMan, self).__init__('Spider-man')

    def web_gun(self):
        print('PIU PIU')

    def web_bomb(self):
        print('Bump')

    def attack(self):
        self.web_gun()

    def ultimate(self):
        self.web_bomb()
