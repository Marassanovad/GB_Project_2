from excep import Excep as ex

class user_interface:
    def Interface(i: str):
        match i:
            case "Welcome":
                print('='*50)
                print('Добро пожаловать в приложение "Заметки"')
                
            case "Menu":
                print('='*50)
                print('Варианты работы программы')
                print('-'*50)
                print('1. Создание, редактирование, удаление заметок')
                print('2. Чтение заметок')
                # print('3. Импорт заметок')
                print('3. Выход из программы')
                
            case "Export":
                print('='*50)
                print('Варианты работы программы')
                print('-'*50)
                print('1. Вывод всех заметок')
                print('2. Вывод заметок по указанным данным')
                print('3. Выход из программы')

            case "Notes_Search":
                print('='*50)
                print('Варианты работы с заметками')
                print('-'*50)
                print('1. По идентификатору')
                print('2. По заголовку')
                print('3. По дате')
                print('4. Выход в главное меню')
                
            case "Mistake":
                print('-'*50)
                print('------ Ошибка -------')
                print('-'*50)
                
            case "Notes_Action":
                print('='*50)
                print('Варианты работы программы')
                print('-'*50)
                print('1. Создать заметку')
                print('2. Редактировать заметку')
                print('3. Удалить заметку')
                print('4. Выход из программы')

            case "Notes_Changes":
                print('='*50)
                print('Варианты изменение заметки')
                print('-'*50)
                print('1. По идентификатору')
                print('2. По заголовоку')
                print('3. По дате')
                print('4. Выход из программы')
            
            case "Notes_Delete":
                print('='*50)
                print('Варианты удаление заметки')
                print('-'*50)
                print('1. По идентификатору')
                print('2. По заголовку')
                print('3. По дате')
                print('4. Выход в главное меню')
                
            case "End":
                print('='*50)
                print('Выберите дальнейшее действие')
                print('-'*50)
                print('1. Выход в главное меню')
                print('2. Выход из программы')

    def Select_filter(case):
        
        user_interface.Interface(case)
        while (True):
            i = ex.action("пункт")
            if i == "1":
                print('Введите идентификатор для поиска')
                return  int(0) 
                
            elif i == "2":
                print('Введите заголовок для поиска')
                return int(2)
            
            elif i == "3":
                print('Введите дату для поиска')
                return int(1)
            
            elif i == "4":
                print('-'*50)
                print("Программа завершила работу")
                print('-'*50)
                break

            else:
                print('-'*50)
                print("Вы ввели неправильные данные")
                print('-'*50)

       
    

