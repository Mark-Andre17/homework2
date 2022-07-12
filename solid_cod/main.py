from heroes import Superman, SuperHero, SpiderMan
from mass_media import MassMediaNews
from place import Kostroma, Tokyo, Place, Planet


def save_the_place(hero: SuperHero, place: Place):
    hero.find(place)
    hero.attack()
    hero.ultimate()
    MassMediaNews(hero, place).create_news()


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(SpiderMan(), Tokyo())
    print('-' * 20)
    save_the_place(Superman(), Planet())
