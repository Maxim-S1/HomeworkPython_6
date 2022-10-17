# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k. 
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def control_input(text):
    flag = False
    while flag == False:
        user_number = input(text)
        try:
            user_number = int(user_number)
            if 0 < user_number:
                flag = True
                return int(user_number)
        except ValueError:
            flag == False


def polynomial(k, largest, smallest):
    l = [str((randint(smallest, largest))) for i in range(k+1)]

    for i in range(k+1):
        if int(l[i]) == 0:
            if i == k:
                l[i] = " = 0"
            else: continue
        elif i == k-1:
            l[i] += f"*x"
        elif i == k:
            l[i] += " = 0"
        elif int(l[i]) == 1:
            l[i] = f"x^{k-i}"
        else: l[i] += f"*x^{k-i}"

    for i in l:
        if i == "0":
            index = l.index(i)
            del l[index]

    result = " + ".join(l)
    return result

k = control_input('Введите натуральная степень k: ')
largest = 100
smallest = 0

with open('file62.txt', 'w') as data:
    data.write(f'{polynomial(k, largest, smallest)}\n')
    data.write(f'{polynomial(k, largest, smallest)}\n')