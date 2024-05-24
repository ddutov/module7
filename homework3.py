# -*- coding: utf-8 -*-

print('Форматирование строк с спользование % - старый стиль:')
team1_num = 5
print('В команде Мастера кода участников: %s!' % team1_num)
print('-----')
team1_num1 = 5
team1_num2 = 6
print('Итого сегодня в командах участников: %s и %s!' % (team1_num1, team1_num2))
print('----------*----------')
print('Форматирование строк с спользование .format - новый стиль:')
score_2 = 42
print('Команда Волшебники данных решила задач: {}'.format(score_2))
print('-----')
team2_time = 18015.2
print('Волшебники данных решили задачи за: {} с'.format(team2_time))
print('----------*----------')
print('Форматирование строк с спользование f-строк - новейший стиль:')
team_1 = 'Мастера Кода'
team_2 = 'Волшебники Данных'
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
challenge_result = ''
print(f'Команда "{team_1}" решила {score_1} задач затратив {team1_time} c.')
print(f'Команда "{team_2}" решила {score_2} задач затратив {team2_time} c.')
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(challenge_result)
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня командами было решено {tasks_total} задач. В среднем на одну задачу затрачено {time_avg} c.')
