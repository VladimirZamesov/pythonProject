from dcts_for_calc import *
from funcs_for_calc import *

"""Временные параметра для расчета"""
name = 'ООО "Аква-Дельта"'
revs = [26527, 25711, 24772]  # list объемов работ за последние 3 года (тыс.руб)
age_of_comp = 29 * 10  # Количество лет на рынке * 10
comp_capital = 703
total_assets = 19039
cost_of_licenses = 370.5
mtb = 2100
senior_mngr_cnt = 6
h_edu_senior = 5
m_edu_senior = 1
non_edu_senior = 0
exp_senior = 20.6 * 10 # средний стаж руководителей * 10
middle_mngr_cnt = 11
h_edu_middle = 10
m_edu_middle = 1
non_edu_middle = 0
exp_middle = 12.3
arch_avards = 2
degree = 2
article = 129
positive_fb_cnt = 9
breach = 0
contract_cnt = 24
contract_delays = 0
total_exp_cnt = 0
negative_exp_cnt = 0
cert_qms = 1
cert_eco = 1

"""Расчет фактор  x1 'История'
Определяеи сектор экономики в котором находится заявитель,
Получаем словарь для поиска значения по параметру 'comp_sector',
Определяем субфактор x11: 'Количество лет на рынке'."""

comp_sector = get_the_value(max(revs), sectors)
dct = get_dct(comp_sector, MBx11, CBx11, KBx11)
x11 = get_the_value(age_of_comp, dct)

# Расчитываем коэффициент вариации
coef_of_var = (k_variable(revs))
# Получаем словарь необходимый по параметру 'comp_sector'
dct = get_dct(comp_sector, MBx12, CBx12, KBx12)
# Определяем субфактор x11: 'Ритмичность работы' по словарю dct, округляем чтоб получить int
x12 = get_the_value(round(coef_of_var), dct)
# Расчитываем фактор x1 'История'
x1 = ((x11 + x12) / 2) * 0.125

"""Расчет фактора x2 'Средства'"""
dct = get_dct(comp_sector, MB1x21, MB2x21, MB3x21, CBx21, KBx21)  # Получаем необходимый словарь
x21 = get_the_value(mtb, dct)  # Расчитываем субфактор x21 ''

res = round((comp_capital / total_assets), 2) * 100
x22 = get_the_value(res, b5)

dct = get_dct(comp_sector, MB1MB2x23, MB3x23, CBx23, KBx23)
x23 = get_the_value(round(cost_of_licenses), dct)

x2 = (x21 * 0.34 + x22 * 0.33 + x23 * 0.33) * 0.375

"""Расчет фактора x3 'Кадры'"""
z1 = (get_middle_education(senior_mngr_cnt, h_edu_senior, m_edu_senior, non_edu_senior))
x1_31 = get_the_value(z1, b7)
x2_31 = get_the_value(exp_senior, b8)
x31 = (x1_31 + x1_31) * 0.5

x1_32 = get_the_value(exp_middle, b8)
a = get_middle_education(middle_mngr_cnt, h_edu_middle, m_edu_middle, non_edu_middle)
x2_32 = get_the_value(a, b7)
x32 = (x1_32 + x1_32) * 0.5

x33 = 100 if arch_avards else 50 if degree else 0

x3 = (x31 * 0.42 + x32 * 0.42 + x33 * 0.16) * 0.15

"""Расчет фактора x4 "Имидж"""""
x41 = get_the_value(article, b11)

x42 = get_the_value(breach, b12)

lmbd = contract_delays * contract_cnt
x43 = get_the_value(lmbd, b13)

t = negative_exp_cnt / total_exp_cnt if (negative_exp_cnt + total_exp_cnt) != 0 else 0
x44 = get_the_value(t, b14)

x45 = 100 if cert_eco and cert_qms else 50 if cert_qms else 0

x46 = 100 if positive_fb_cnt >= 3 else 50 if 0 < positive_fb_cnt <= 3 else 0

x4 = (x41 * 0.2 + x42 * 0.15 + x43 * 0.15 + x44 * 0.15 + x45 * 0.2 + x46 * 0.15) * 0.35

R = sum([x1, x2, x3, x4])

print(f'Индекс деловой репуткции {name} - {round(R)}')
