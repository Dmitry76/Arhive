#МОДУЛИ И БИБЛИОТЕКИ
import random

# СОЗДАЕМ ЧИСТЫЙ ЛИСТ
paper = {'00': '-', '01': '-', '02': '-', '10': '-', '11': '-', '12': '-', '20': '-', '21': '-', '22': '-'}
fields = ('00', '01', '02', '10', '11', '12', '20', '21', '22')
game_status = 'start'  # устанавливаем начальный статус
game_result = ''
last_action = {'11': '02', '12': '00', '13': '01',
               '21': '12', '22': '10', '23': '11',
               '31': '22', '32': '20', '33': '21',
               '41': '20', '42': '00', '43': '10',
               '51': '21', '52': '01', '53': '11',
               '61': '22', '62': '02', '63': '12',
               '71': '22', '72': '00', '73': '11',
               '81': '02', '82': '20', '83': '11'}  # ВАРИАНТЫ ПОСЛЕДНЕГО ВЫИГРЫШНОГО ХОДА

second_action = {'11': ['01', '02'], '12': ['00', '02'], '13': ['00', '01'],
                 '21': ['11', '12'], '22': ['10', '12'], '23': ['10', '11'],
                 '31': ['21', '22'], '32': ['20', '22'], '33': ['20', '21'],
                 '41': ['10', '20'], '42': ['00', '20'], '43': ['00', '10'],
                 '51': ['11', '21'], '52': ['01', '21'], '53': ['01', '11'],
                 '61': ['12', '22'], '62': ['02', '22'], '63': ['02', '12'],
                 '71': ['11', '22'], '72': ['00', '22'], '73': ['00', '11'],
                 '81': ['11', '02'], '82': ['20', '02'], '83': ['20', '11']}  # ВАРИАНТЫ ТОРОГО ХОДА


# ФУНКЦИИ:
# ==ВЕРСТКА ИГРОВОГО ПОЛЯ ДЛЯ ВЫВОДА В КОНСОЛЬ
def show_paper():
    global paper
    a = '  0 1 2\n0 '
    a += paper['00']
    a += ' ' + paper['01']
    a += ' ' + paper['02']
    a += '\n1 ' + paper['10']
    a += ' ' + paper['11']
    a += ' ' + paper['12']
    a += '\n2 ' + paper['20']
    a += ' ' + paper['21']
    a += ' ' + paper['22']
    return a


# ==СКАНИРОВАНИЕ ВЫИГРЫШНЫХ КОМБИНАЦИЙ
def result_scan():
    global paper
    rs = [str(paper['00'] + paper['01'] + paper['02']),
          str(paper['10'] + paper['11'] + paper['12']),
          str(paper['20'] + paper['21'] + paper['22']),
          str(paper['00'] + paper['10'] + paper['20']),
          str(paper['01'] + paper['11'] + paper['21']),
          str(paper['02'] + paper['12'] + paper['22']),
          str(paper['00'] + paper['11'] + paper['22']),
          str(paper['20'] + paper['11'] + paper['02'])]
    return rs


# ======Приглашение в игру
print('Выберите:\n"X" - начинает первым\n"O" - делает ход вторым')
gamer_symbol = str(input('Чем будете играть? '))

# ПРОВЕРКА ВВОДА
if gamer_symbol == 'X' or gamer_symbol == 'x' or gamer_symbol == 'Х' or gamer_symbol == 'х':
    gamer = ['X']
    comp = ['O']
    print('Вы выбрали "X", делайте первый ход!\n')
else:
    print('Вы не выбрали "X", первый ход за мной!\n')
    gamer = ['O']
    comp = ['X', '11']
    paper['11'] = 'X'

while game_status == 'start':
    print(show_paper())  # ВЫВОД ИГРОВОГО ПОЛЯ В КОНСОЛЬ

    print('Введите координаты Вашего хода в виде двухзначного числа в формате: VG (V-вертикаль, G-горизонталь)')
    print('ВНИМАНИЕ! НЕВЕРНЫЕ КООРДИНАТЫ = ПРОПУСК ХОДА!!!')
    gamer_action = str(input('Ваш ход: '))
    gamer.append(gamer_action)
    comp_action = '0'  # ХОД не сделан
    # ПРОВЕРКА ЗАНЯТО ЛИ МЕСТО КОМПЬЮТЕРОМ
    for x in comp:
        if x == gamer_action:
            print('Это место занято!\n')
            gamer_action = '99'
            gamer[(len(gamer) - 1)] = '99'
    paper[gamer_action] = gamer[0]

    # ПРОВЕРКА ОКОНЧАНИЯ ИГРЫ==================================

    result = result_scan()  # СКАНИРОВАНИЕ ВЫИГРЫШНЫХ КОМБИНАЦИЙ

    # ПРОВЕРКА ВЫИГРЫША ИГРОКА ИЛИ КОМПЬЮТЕРА
    for x in result:
        if x == str(gamer[0] + gamer[0] + gamer[0]):
            game_result = '\nПОЗДРАВЛЯЮ! Победа за Вами!!!'
            game_status = 'END'  # статус для выхода из цикла
        if x == str(comp[0] + comp[0] + comp[0]):
            game_result = '\nМоя взяла!!!'
            game_status = 'END'  # статус для выхода из цикла
    # ==========================================================

    # ГЕНЕРАТОР ХОДА КОМПЬЮТЕРА
    # 1. ПРОВЕРКА СТАТУСА ИГРЫ (game_status == 'start')

    if game_status == 'start':
        # 2. Если не занято место в центре (11), занимаем
        if result[1][1] == '-':
            comp.append('11')
            paper['11'] = comp[0]
            comp_action = '1'  # ХОД сделан

        result = result_scan()  # СКАНИРОВАНИЕ ВЫИГРЫШНЫХ КОМБИНАЦИЙ
        # print('#3 Комбинации:', result)
        # 3. Если есть вариант закончить с победой: 'XX-', '-XX' или 'X-X', то заканчиваем игру
        # print('# 3.', comp_action)
        for i in range(0, len(result)):
            if result[i] == comp[0] + comp[0] + '-' and comp_action == '0':  ## XX-
                comp.append(last_action[str(i + 1) + '1'])
                paper[last_action[str(i + 1) + '1']] = comp[0]
                comp_action = '1'  # ХОД сделан
                game_result = '\nМоя взяла!!!'
                game_status = 'END'  # статус для выхода из цикла
                # print('XX- Статистика ходов компа:', comp)
            if result[i] == '-' + comp[0] + comp[0] and comp_action == '0':  ## -XX
                comp.append(last_action[str(i + 1) + '2'])
                paper[last_action[str(i + 1) + '2']] = comp[0]
                comp_action = '1'  # ХОД сделан
                game_result = '\nМоя взяла!!!'
                game_status = 'END'  # статус для выхода из цикла
                # print('-XX Статистика ходов компа:', comp)
            if result[i] == comp[0] + '-' + comp[0] and comp_action == '0':  ## X-X
                comp.append(last_action[str(i + 1) + '3'])
                paper[last_action[str(i + 1) + '3']] = comp[0]
                comp_action = '1'  # ХОД сделан
                game_result = '\nМоя взяла!!!'
                game_status = 'END'  # статус для выхода из цикла
                # print('X-X Статистика ходов компа:', comp)

        result = result_scan()  # СКАНИРОВАНИЕ ВЫИГРЫШНЫХ КОМБИНАЦИЙ
        # print('#4 Комбинации:', result)
        # print('# 4.', comp_action)
        # 4. Если игрок близок к победе: 'XX-', '-XX' или 'X-X', то закрываем пустое место
        for i in range(0, len(result)):
            if result[i] == gamer[0] + gamer[0] + '-' and comp_action == '0':  ## XX-
                comp.append(last_action[str(i + 1) + '1'])
                paper[last_action[str(i + 1) + '1']] = comp[0]
                comp_action = '1'  # ХОД сделан
                # print('XX- Статистика ходов компа:', comp)
            if result[i] == '-' + gamer[0] + gamer[0] and comp_action == '0':  ## -XX
                comp.append(last_action[str(i + 1) + '2'])
                paper[last_action[str(i + 1) + '2']] = comp[0]
                comp_action = '1'  # ХОД сделан
                # print('-XX Статистика ходов компа:', comp)
            if result[i] == gamer[0] + '-' + gamer[0] and comp_action == '0':  ## X-X
                comp.append(last_action[str(i + 1) + '3'])
                paper[last_action[str(i + 1) + '3']] = comp[0]
                comp_action = '1'  # ХОД сделан
                # print('X-X Статистика ходов компа:', comp)

        result = result_scan()  # СКАНИРОВАНИЕ ВЫИГРЫШНЫХ КОМБИНАЦИЙ
        # print('#5 Комбинации:', result)
        # print('# 5.', comp_action)
        # 5. Продолжаем любой вариант: 'X--', '-X-' или '--X'
        varik = []
        for i in range(0, len(result)):
            if result[i] == comp[0] + '--' and comp_action == '0':  ## X--
                for ii in second_action[str(i + 1) + '1']:
                    varik.append(ii)
                    # print('X--', ii)
            if result[i] == '-' + comp[0] + '-' and comp_action == '0':  ## -X-
                for ii in second_action[str(i + 1) + '2']:
                    varik.append(ii)
                    # print('-X-', ii)
            if result[i] == '--' + comp[0] and comp_action == '0':  ## --X
                for ii in second_action[str(i + 1) + '3']:
                    varik.append(ii)
                    # print('--X', ii)
        if not varik and comp_action == '0':
            for i in fields:
                if paper[i] == '-':
                    varik.append(i)
            if not varik and comp_action == '0':
                game_result = '\nПохоже ничья...'
                game_status = 'END'  # статус для выхода из цикла
            elif varik and comp_action == '0':
                rnd = random.random()
                comp.append(varik[int(rnd * len(varik) // 1)])
                paper[varik[int(rnd * len(varik) // 1)]] = comp[0]
        elif varik and comp_action == '0':
            rnd = random.random()
            comp.append(varik[int(rnd*len(varik) // 1)])
            paper[varik[int(rnd*len(varik) // 1)]] = comp[0]
        # print('Варианты хода компа: ', str(varik))
    # ТЕСТИРОВАНИЕ ВНУТРИ ЦИКЛА========================================
    # print(result)
    # print('Элементов в списке: ' + str(len(gamer)) + '\n' + str(gamer))
    # =================================================================

# ВЫВОД РЕЗУЛЬТАТА ИГРЫ
print(game_result)
print(show_paper())
# ========================
