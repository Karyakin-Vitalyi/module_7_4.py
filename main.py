# Домашнее задание по теме "Форматирование строк"

# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Определение результата соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Форматирование строк с использованием %
formatted_team1 = "В команде Мастера кода участников: %d !" % team1_num
formatted_total = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

# Форматирование строк с использованием format()
formatted_score_2 = "Команда Волшебники данных решила задач: {} !".format(score_2)
formatted_time_2 = "Волшебники данных решили задачи за {} с !".format(team2_time)

# Форматирование строк с использованием f-строк
formatted_scores = f"Команды решили {score_1} и {score_2} задач."
formatted_challenge_result = f"Результат битвы: {challenge_result}"
formatted_tasks_info = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"

# Вывод результатов
print(formatted_team1)
print(formatted_total)
print(formatted_score_2)
print(formatted_time_2)
print(formatted_scores)
print(formatted_challenge_result)
print(formatted_tasks_info)




