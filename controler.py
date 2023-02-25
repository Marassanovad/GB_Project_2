from interface import user_interface as console
from excep import Excep as ex
from model.action import action as act
from model import export as exp

path = 'note.csv'
def main(path):
    console.Interface("Welcome")
    while(True):
        console.Interface("Menu")
        i = ex.action("пункт")
        match i:
            case "1": 
                console.Interface("Notes_Action")
                i = ex.action("пункт")
                if i == "1":#create
                    print('-'*50)
                    print('Вы выбрали "Создать заметку"')
                    print('-'*50)
                    act.create_note()

                elif i == "2": #change
                    print('-'*50)
                    print('Вы выбрали "Редактировать заметку"')
                    print('-'*50)
                    x = console.Select_filter("Notes_Changes")
                    act.change_note(path, x)
                    
                elif i == "3": #delete
                    print('-'*50)
                    print('Вы выбрали "Удалить заметку"')
                    print('-'*50)
                    x = console.Select_filter("Notes_Delete")
                    act.delete_note(path, x)

                elif i == "4":
                    print('-'*50)
                    print("Программа завершила работу")
                    print('-'*50)
                    break
                else:
                    print('-'*50)
                    print("Вы ввели неправильные данные")
                    print('-'*50)
               
            case "2":
                console.Interface("Export")
                i = ex.action("пункт")
                if i == "1":
                    print('-'*50)
                    print('Вы выбрали "Вывод всех данных"')
                    print('-'*50)
                    exp.show_all_notes(path)

                #доделать  
                elif i == "2": 
                    print('-'*50)
                    print('Вы выбрали " Вывод заметок по указанным данным"')
                    print('-'*50)
                    exp.selected_filter(path)
                elif i == "3":
                    print('-'*50)
                    print("Программа завершила работу")
                    print('-'*50)
                    break
                else:
                    print('-'*50)
                    print("Вы ввели неправильные данные")
                    print('-'*50)
                
        
            case "3":
                print('-'*50)
                print("Программа завершила работу")
                print('-'*50)
                break
            case _: 
                print('-'*50)
                print("Не корректный ввод")

main(path)