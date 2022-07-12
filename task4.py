import time


def repeat_func(call_count, start_sleep_time, factor, border_sleep_time):
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            result_time = start_sleep_time
            print(f'Кол-во запусков = {call_count}')
            print('Начало работы')
            for i in range(call_count):
                func_result = func(*args, **kwargs)
                if result_time < border_sleep_time:
                    result_time = start_sleep_time * factor ** i
                else:
                    result_time = border_sleep_time
                print(f'Запуск номер {i + 1}. Ожидание: {result_time} секунд. Результат декорируемой функций = {func_result}.')
                time.sleep(result_time)
            print('Конец работы')
            return
        return wrapper
    return func_decorator


if __name__ == '__main__':
    @repeat_func(3, 1, 2, 4)
    def print_something():
        return f'поехали!!!'

    print(print_something())
