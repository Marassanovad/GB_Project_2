from datetime import datetime as dt

class logg:
    def actions_logger(data):
        time = dt.now().strftime('%D %H:%M')
        with open('log.csv', 'a', encoding='utf-8') as file:
            file.write(f'{data}, {time} \n')
            
    def entered_logger(data): # лог ввода от пользователя
        time = dt.now().strftime('%D  %H:%M')
        with open('log.csv', 'a', encoding='utf-8') as file:
            file.write('{}   Данные от пользователя: {}\n'.format(time, data))
