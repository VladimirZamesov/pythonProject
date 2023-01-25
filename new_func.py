import math


def get_the_value(user_sector, d):  # Основная функция для получения значения по словарю
    for i, x in enumerate(d):
        if i == len(d) - 1:
            return d['last']
        elif user_sector in x:
            return d[x]


def k_variable(user_rev, res=0):  # Расчет коэффициента вариации
    z = sum(user_rev) / len(user_rev)
    for i in range(len(user_rev)):
        res += (user_rev[i] - z) ** 2
    return ((res / len(user_rev)) ** 0.5) / z


def get_dct(user_sector, *args):  # args: словари по порядку от МБ1 до КБ3
    for d in args:
        if user_sector in d['key']:
            d.pop('key')
            return d


# def get_round_num(number, decimals=0):  # Округление float числа с заданным количеством знаков после запятой
#     decimal_places = 10 ** decimals
#     return math.floor(number * decimal_places + 0.5) / decimal_places


def get_middle_exp(user_cnt_seniors, *args):  # args: количество сотрудников, имеющих образхование (в, с, б/о)
    return round(((args[0] + args[1] * 0.5) / user_cnt_seniors), 2)

