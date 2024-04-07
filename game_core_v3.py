import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    
def game_core_v3(number: int=1) -> int:
    """Подход 3: Угадывание с помощью алгоритма бинарного поиска
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Число попыток.
    min_value = 0 # Минимальное значение интервала выборки.
    max_value = 100 # Максимальное значение интервала выборки.
    predict = 0 # Число текущего предположения.

    while number != predict:
        count += 1
        predict = (min_value+max_value) // 2
        
        if number > predict:
            min_value = predict + 1
        elif number < predict:
            max_value = predict - 1
            
    return count

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)