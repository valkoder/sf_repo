import numpy as np


def game_core_v3(number):
    right = 100                                      # верхняя граница интервала
    left = 0                                         # нижняя граница интервала
    count = 0                                        # сброс счетчика
    predict = 0
    while number != predict:
        count += 1
        predict = round((left + right) / 2.0)
        if predict < number:
            left = predict
            predict = round((left + right) / 2.0)
        elif predict > number:
            right = predict
            predict = round((left + right) / 2.0)
    return count                                 # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = float(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score:.2f} попыток")
    return score


score_game(game_core_v3)                               # запускаем
