def get_the_value(user_param, dct):
    """
    Функция определяет значение в словаре по параметру компании.
    Args:
        user_param: (int) параметр компании - значние для поиска по ключу,
        dct: (dict) необходимый словарь. В качестве ключа используются диапазоны range.

    Returns: (str or int)

    """
    for i, x in enumerate(dct):
        if i == len(dct) - 1:
            return dct['last']
        elif user_param in x:
            return dct[x]


def k_variable(user_rev, res=0):
    """
    Функция для расчета коэффициента вариации
    Args:
        user_rev: (list) объем работ (тыс. руб) по годам за оцениваемый период (max len == 3).
        res: промежуточный результат расчета

    Returns: (float)

    """
    for i in range(len(user_rev)):
        res += (user_rev[i] - (sum(user_rev) / len(user_rev))) ** 2
    return ((res / len(user_rev)) ** 0.5) / (sum(user_rev) / len(user_rev)) * 1000


def get_dct(user_sector, *args):
    """
    Функция подбора нужного словаря из модуля 'dcts_for_calc'
    Args:
        user_sector: (str) сегмент рынка, занимаемый организацией,
        определяется с помощью функции 'get_the_value' или вводится вручную
        *args: (dict) перечень словарей, передаются в порядке от MB1 до KB3

    Returns:(dict)

    """
    for d in args:
        if user_sector in d['key']:
            d.pop('key')
            return d


# def get_round_num(number, decimals=0):  # Округление float числа с заданным количеством знаков после запятой
#     decimal_places = 10 ** decimals
#     return math.floor(number * decimal_places + 0.5) / decimal_places


def get_middle_education(staff_cnt, *args):
    """
    Функция расчета доли сотрудников имеющих высшее образование
    Args:
        staff_cnt: (int) общее число сотрудников
        *args: (int) количество сотрудников имебщих.
         1. высшее образование
         2. среднее образование
         3. образование отсутствует
         передаются в порядке от 1 к 3

    Returns: (int, float)

    """
    return (round(((args[0] + args[1] * 0.5) / staff_cnt), 2)) * 100
