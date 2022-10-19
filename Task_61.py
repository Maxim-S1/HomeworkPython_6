# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.


field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
     
def print_field(field):
    for i in field:
        print(i)

print('Игровое поле')
print_field(field)


# from random import randint
# Name1 = str(input("Введите имя первого игрока: "))
# Name2 = str(input("Введите имя второго игрока: "))
# A = randint(1, 6)
# B = randint(1, 6)
# print(f'{Name1} выкинул число: {A}')
# print(f'{Name2} выкинул число: {B}')
# while A == B:
#     print('Нужно повторить вбрасывание кубиков')
#     break
# if A > B: print(f'{Name1} ходит крестиком. {Name2} ходит ноликом')    
# if A < B: print(f'{Name2} ходит крестиком. {Name1} ходит ноликом')

def fill_num_in_field1(field, n):
    for el in field:
        for i in range(len(field)):
            if el[i] == n:
                el[i] ='x'

def fill_num_in_field2(field, k):
    for el in field:
        for i in range(len(field)):
            if el[i] == k:
                el[i] ='0'

# def check_field1(field):
    # for el in field:
    #     for i in range(len(field)):
    #         if el[i] =='x' and el[i+1] == 'x' and el[i+2] =='x':
    #             print('Победил игрок который ходит крестком')
    #             break
    #         if el[i] =='0' and el[i+1] == '0' and el[i+2] =='0':
    #             print('Победил игрок который ходит ноликом')
    #             break
def check_field2(field):
    for i in range(1, len(field)+1):
        for j in range(1, len(field)+1):
            if (field[i][j] == 'x' and field[i + 1][j] == 'x' and field[i + 2][j] == 'x') \
                or (field[i][j] == 'x' and field[i][j+1] == 'x' and field[i][j+2] == 'x') \
                or (field[0][0] == 'x' and field[1][1] == 'x' and field[2][2] == 'x')\
                or (field[0][2] == 'x' and field[1][1] == 'x' and field[2][0] == 'x'):
                print('Победил игрок который ходит крестком')
                # break
            if field[i][j] == '0' and field[i + 1][j] == '0' and field[i + 2][j] == '0' \
                or (field[i][j] == '0' and field[i][j+1] == '0' and field[i][j+2] == '0') \
                or (field[i][j] == '0' and field[i+1][j+1] == '0' and field[i+2][j+2] == '0')\
                or (field[i][j+2] == '0' and field[i+1][j+1] == '0' and field[i][j+2] == '0'):
                print('Победил игрок который ходит ноликом')
                # break

for i in range(5):
    a = int(input("Введите цифру, куда хотите поставить крестик: "))
    fill_num_in_field1(field, a)
    print_field(field)
    # check_field1(field)
    check_field2(field)
    b = int(input("Введите цифру, куда хотите поставить нолик: "))
    fill_num_in_field2(field, b)
    print_field(field)
    # check_field1(field)
    check_field2(field)


