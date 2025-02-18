from itertools import *
def zad1():
    """ Returns:
        str: Строка с ответом.
        >>> zad1()
        'Ответ: 175'
        """

    slovo = ['И', 'В', 'А', 'Н']
    slovo_vars = product(slovo, repeat = 4)
    count = 0
    for var in slovo_vars:
        if 'И' in var:
            # print("".join(var))
            count += 1
    return(f"Ответ: {count}")

def zad2():
    """ Returns:
        str: Строка с ответом.
        >>> zad2()
        'Ответ: 150'
        """
    number = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255
    octal_number = oct(number)[2:]
    count = octal_number.count('0')
    return(f"Ответ: {count}")


def zad3():
    """ Returns:
        str: Строка с ответом.
        >>> zad3()
        'Ответ: 72, 84084'
        """
    max_count = 0
    for x in range(84052, 84131):
        count = 0
        for y in range(1, x+1):
            if x % y == 0:
                count += 1
                #print(x, y, x / y, count)
        if count > max_count:
            max_count = count
            min_x = x
        elif count == max_count:
            min_x = min(min_x, x)
    return(f"Ответ: {max_count}, {min_x}")

print(f"Задание 1: Подсчет количества слов, содержащих 'И', {zad1()}")
print(f"Задание 2: Подсчет количества нулей в восьмеричной записи числа, {zad2()}")
print(f"Задание 3: Найти наибольшее количество делителей в диапазоне от 84052 до 84130, {zad3()}")

if __name__=="__main__":
    import doctest
    doctest.testmod()