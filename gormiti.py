#Chipicao Gormiti
import random
import time
import os
import pyttsx3

engine = pyttsx3.init()

hero = ["Алфа", "Риф", "Трек", "Айкор", "Кратус"]

def comp():
    strategy1 = [random.randint(10, 100) for i in range(1)]
    print(f"Стратегия: {strategy1}")
    skill1 = [random.randint(10, 100) for i in range(1)]
    print(f"Умение: {skill1}")
    power1 = [random.randint(10, 100) for i in range(1)]
    print(f"Cила: {power1}")
    wisdom1 = [random.randint(10, 100) for i in range(1)]
    print(f"Ум: {wisdom1}")
    heroes1 = random.choice(hero)
    return (strategy1, skill1, power1, wisdom1, heroes1)

def human():
    strategy2 = [random.randint(10, 100) for i in range(1)]
    print(f"Стратегия: {strategy2}")
    skill2 = [random.randint(10, 100) for i in range(1)]
    print(f"Умение: {skill2}")
    power2 = [random.randint(10, 100) for i in range(1)]
    print(f"Cила: {power2}")
    wisdom2 = [random.randint(10, 100) for i in range(1)]
    print(f"Ум: {wisdom2}")
    heroes2 = random.choice(hero)
    return (strategy2, skill2, power2, wisdom2, heroes2)

while True:
    time.sleep(3)
    print("-" * 20)
    print("Игрок: Компьютер. Начинаеться выбор персонажа.... ")
    engine.say("Игрок: Компьютер. Начинаеться выбор персонажа.... ")
    engine.runAndWait()
    print("")
    str1, sk1, pow1, wis1, hero1 = comp()
    comp1 = str1[0] + sk1[0] + pow1[0] + wis1[0]
    print("")
    print(f"{hero1} количество очков: {comp1}")
    engine.say(f"{hero1} количество очков: {comp1}")
    engine.runAndWait()
    print("")
    time.sleep(5)
    print("-" * 20)
    print(f"Игрок: Человек. Начинаеться выбор персонажа.... ")
    engine.say("Игрок: Человек. Начинаеться выбор персонажа.... ")
    engine.runAndWait()
    print("")
    str2, sk2, pow2, wis2, hero2 = human()
    human1 = str2[0] + sk2[0] + pow2[0] + wis2[0]
    print("")
    print(f"{hero2} количество очков: {human1}")
    engine.say(f"{hero2} количество очков: {human1}")
    engine.runAndWait()
    print("")
    time.sleep(5)
    if comp1 > human1:
        print(f"Выйграл {hero1} с перевесом в {comp1 - human1} очков.")
        engine.say(f"Выйграл {hero1} с перевесом в {comp1 - human1} очков.")
        engine.runAndWait()
        if hero1 == "Алфа":
            os.startfile(r'C:\Users\Dester\Pictures\гормити\alfa.jpg')
        if hero1 == "Риф":
            os.startfile(r'C:\Users\Dester\Pictures\гормити\riff.jpg')
        if hero1 == "Трек":
            os.startfile(r'C:\Users\Dester\Pictures\гормити\trek.jpg')
        if hero1 == "Айкор":
            os.startfile(r'C:\Users\Dester\Pictures\гормити\aikor.jpg')
        if hero1 == "Кратус":
            os.startfile(r'C:\Users\Dester\Pictures\гормити\kratus.jpg')
        time.sleep(5)
        print("-" * 20)
        ex = int(input("Хотите продолжить?:\n1) Да - 1\n2) Нет - 2\nВведите ваш выбор: "))
        engine.say("Хотите продолжить?")
        engine.runAndWait()
        if ex == 1:
            print("Продолжаем игру.")
            engine.say("Продолжаем игру.")
            engine.runAndWait()
            continue
        elif ex == 2:
            print("Игра окончена.")
            engine.say("Игра окончена.")
            engine.runAndWait()
            break
        else:
            print("Неверная команда. Введите: 1 или 2")
            print("-" * 20)
    elif comp1 < human1:
        print(f"Выйграл {hero2} с перевесом в {human1 - comp1} очков.")
        engine.say(f"Выйграл {hero2} с перевесом в {human1 - comp1} очков.")
        engine.runAndWait()
        if hero2 == "Алфа":
            os.startfile(r'C:\Users\Dester\Pictures\гормити\alfa.jpg')
        if hero2 == "Риф":
            os.startfile(r'C:\Users\Dester\Pictures\гормити\riff.jpg')
        if hero2 == "Трек":
            os.startfile(r'C:\Users\Dester\Pictures\гормити\trek.jpg')
        if hero2 == "Айкор":
            os.startfile(r'C:\Users\Dester\Pictures\гормити\aikor.jpg')
        if hero2 == "Кратус":
            os.startfile(r'C:\Users\Dester\Pictures\гормити\kratus.jpg')
        time.sleep(5)
        print("-" * 20)
        ex = int(input("Хотите продолжить?:\n1) Да - 1\n2) Нет - 2\nВведите ваш выбор: "))
        engine.say("Хотите продолжить?")
        engine.runAndWait()
        if ex == 1:
            print("Продолжаем игру.")
            engine.say("Продолжаем игру.")
            engine.runAndWait()
            continue
        elif ex == 2:
            print("Игра окончена.")
            engine.say("Игра окончена.")
            engine.runAndWait()
            break
        else:
            print("Неверная команда. Введите: 1 или 2")
            print("-" * 20)
    else:
        print("Ничья")
        time.sleep(5)
