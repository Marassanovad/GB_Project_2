from logg import logg
from datetime import datetime as dt
import sys
import os

class Excep:
    def action(desc: str):
        while(True):
            i = input('Введите {}: '.format(desc)) 
            if i.isdigit():
                logg.entered_logger(i)
                return i
            print("Это не корректный ввод")
            text = "Пользователь ввел: " + i + ". Это некорректный ввод"
            logg.actions_logger(text)
    
        # ввод данных пользователем
    def input_data():
        id = Excep.action("ID: ")
        time = dt.now().strftime('%D')
        main_note = Excep.check_input_string('Заголовок: ')
        note= Excep.check_input_string('Заметка: ')
        return [id, time, main_note, note]

# ввод данных и проверка строковых данных(оптимизация кода)
    def check_input_string(desc: str):
        while True:
            val = input('Введите {}: '.format(desc))
            if len(val) < 1: # or not val.isalpha():
                print('Поле "{}" должно быть не пустым.'.format(desc))
                logg.actions_logger ('Пользователь ввел некорректные данные')
                continue
            return val
    
    def digit(x):
        while(True):
            i = input("Введите выбранный пункт: ")
            if i.isdigit():
                i = int(i)
                if i < x+1:
                    logg.entered_logger(i)
                    return i
                else: 
                    print("Вам надо ввести число из диапазон")
                    continue
            print("Вам надо ввести число")
            text = "Пользователь ввел: " + i + ". Это некорректный ввод"
            logg.actions_logger(text)

    def read_file_except(file_path):
        if not os.path.exists(file_path):
            print(f'Файл не найден или некорректно указан путь: {file_path}')
            sys.exit()