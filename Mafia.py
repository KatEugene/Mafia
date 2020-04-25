from random import choice

# Подготовка данных

list_of_players = ['Беляева Полина',
                   'Будаева Дарья',
                   'Вольнов Никита',
                   'Габриелян Ваге',
                   'Гузеватый Роман',
                   'Гусева Екатерина',
                   'Докучаев Олег',
                   'Казачков Федор',
                   'Калмыков Владимир',
                   'Карасёв Никита',
                   'Катасонов Евгений',
                   'Кириллов Дмитрий',
                   'Кожевников Михаил',
                   'Косенко Сёмен',
                   'Кудрявцев Андрей',
                   'Медведев Вячеслав',
                   'Митрофанов Матвей',
                   'Овсяников Алексей',
                   'Осина Мария',
                   'Пажетных Мария',
                   'Рубекина Евгения',
                   'Семенихин Кирилл',
                   'Семенова Надежда',
                   'Семчишин Степан',
                   'Спиридонова Ирина',
                   'Ступницкий Михаил',
                   'Фокина Ксения',
                   'Хозинский Артем',
                   'Шевченко Илья',
                   'Штарев Владимир']

roles = ['Дон мафии',
         'Мафия',
         'Маньяк',
         'Путана',
         'Комиссар',
         'Доктор',
         'Мирный житель']

players_in_game = []
count_of_roles = [0] * 7

for player in list_of_players:
    playing = input(f"{player}: ")
    if playing == "1":
        players_in_game.append(player)

for index in [0, 2, 3, 4, 5]:
    count_of_roles[index] = 1

if len(players_in_game) <= 12:
    count_of_roles[1] = 2
elif len(players_in_game) <= 18:
    count_of_roles[1] = 3
elif len(players_in_game) <= 30:
    count_of_roles[1] = 4

count_of_roles[-1] = len(players_in_game) - sum(count_of_roles)

player_and_role = {}

for role_i in range(len(roles)):
    role = roles[role_i]
    for _ in range(count_of_roles[role_i]):
        random_player = choice(players_in_game)
        players_in_game.remove(random_player)
        if role not in player_and_role.keys():
            player_and_role[role] = [random_player]
        else:
            player_and_role[role] = player_and_role.get(role) + [random_player]

print()
[print(elem, player_and_role.get(elem)) for elem in player_and_role.keys()]
print()

players_stats = []
for role_j in player_and_role.keys():
    for player_j in player_and_role.get(role_j):
        players_stats.append([player_j, role_j, 1])

# Игровой процесс


def count_civil():
    counter = 0
    for elem in players_stats:
        if elem[2] == 1 and (elem[1] != 'Мафия' and elem[1] != "Дон мафии" and elem[1] != "Маньяк"):
            counter += 1
    return counter


def count_mafia():
    counter = 0
    for elem in players_stats:
        if elem[2] == 1 and (elem[1] == 'Мафия' or elem[1] == "Дон мафии"):
            counter += 1
    return counter


def maniac():
    man = False
    counter = 0
    for elem in players_stats:
        if elem[2] == 1:
            counter += 1
        if elem[1] == "Маньяк" and elem[2] == 1:
            man = True
    return man and counter == 2


def main():
    day = 1

    while (count_civil() > count_mafia()) and (not maniac()):
        print(f"Night {day}")

        killed_by_mafia = input("Кого сегодня убили мафия? ")
        killed_by_maniac = input("Кого сегодня убил маньяк? ")
        treated = input("Кого сегодня лечили? ")
        checked = input("Кого сегодня проверял шериф? ")
        puta_person = input("К кому на вечер уходила путана? ")
        
        for i in range(len(players_stats)):
            elem = players_stats[i]
            if (elem[0] == killed_by_mafia or elem[0] == killed_by_maniac) and (elem[0] != treated) and (elem[0] != puta_person):
                elem[2] = 0
                
            if (elem[0] == killed_by_mafia or elem[0] == killed_by_maniac) and elem[1] == "Путана":
                elem[2] = 0
                for i in range(len(players_stats)):
                    if players_stats[i][0] == puta_person and players_stats[i][0] != treated:
                        players_stats[i][2] = 0
                
            if elem[0] == checked:
                print(f"Информация для шерифа: {elem[0]} - {elem[1].upper()}")

        killed_by_people = input("Кого сегодня убили голосованием? ")

        for i in range(len(players_stats)):
            if players_stats[i][0] == killed_by_people:
                players_stats[i][2] = 0
                
        day += 1

        [print(elem) for elem in players_stats]
        print()

# Запускай если лень самому следить за ролями


main()
