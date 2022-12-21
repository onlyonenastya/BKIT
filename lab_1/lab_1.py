import sys
import math

def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    while True:
        try:
            float(coef_str)
            break
        except:
            coef_str = input()
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        t = -b / (2.0 * a)
        result.append(math.sqrt(t))
        result.append(-math.sqrt(t))
    elif D > 0.0:
        sqD = math.sqrt(D)
        t1 = ((-b + sqD) / (2.0 * a))
        t2 = ((-b - sqD) / (2.0 * a))
        if (t1 >= 0):
            result.append(-math.sqrt(t1))
            result.append(math.sqrt(t1))
        if (t2 >= 0):
            result.append(-math.sqrt(t2))
            result.append(math.sqrt(t2))
    return result


def main():
    while True:
        a = get_coef(1, 'Введите коэффициент А:')
        if a !=0:
            break
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    # Вывод корней
    roots = sorted(list(set(roots)))
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {}, {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {}, {}'.format(roots[0], roots[1], roots[2], roots[3]))

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()