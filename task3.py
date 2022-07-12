def save_cached(func):
    final_dict = {}

    def wrapper(number):
        if not final_dict.get(number):
            final_dict[number] = func(number)
        return final_dict[number]

    return wrapper


@save_cached
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    print(multiplier(5))
    print(multiplier(3))
    print(multiplier(4))

    print(id(multiplier(3)))
    print(id(multiplier(4)))
    print(id(multiplier(3)))
    print(id(multiplier(4)))
