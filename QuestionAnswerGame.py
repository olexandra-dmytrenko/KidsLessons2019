#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8
import random

questions = ["What's your name",
             "How old are you",
             "Where do you live",
             "What's the weather like today",
             "Do you like me",
             "How can I get to the post office",
             "Who drank from my cup"
             ]
answers = ["That is too complicated to tell",
           "Let's better ask my friend",
           "Better ask my yourself",
           "Tomorrow it will be different anyway",
           "You don't want to know that",
           "Thinking of that makes me sad",
           "You know it yourself",
           "You don't need to know it",
           "Be nice",
           "Go straight till the road crossing"
           ]
random.shuffle(questions)
random.shuffle(answers)

for item in range(4):
    print(str(item + 1) + ".\n"
        "Mom: " + questions[item] + "?\n"
        "Me: " + answers[item] + "."
        "\n----------------------------------")

# Этапы работы:
# 1) написать массивы
# 2) написать вывод первых значений вопроса и ответа. Обосновать, что сначало надо задача чтоб работала, потом украшать.
# 3) Написать цикл с выводом вопросов - ответов по очереди.
# 4) добавить перемешивание массивов
# 5)сделать вывод на экран красивее, добавить нумерацию
#
# // Вопросы к программе
# 1) что будет, если количество значений в массивах не одинаковое?
# 2) что если не перемешать массив, а каждый раз брать случайный ответ / вопрос?