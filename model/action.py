# from excep import Excep as ex
from excep import Excep as ex
import csv
from model import export as exp
# from interface import user_interface as console
from model import action as act
from model import imp as imp


class action:
    # создание заметки
    def create_note():
        ls = ex.input_data()
        with open('note.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(ls)

    # редактирование заметки
    def change_note(path, x):
        index_list = []
        list_note = exp.read_data(path)
        # print('Введите параметры поиска: ')
        change_filter = ex.check_input_string('ваши параметры')
        i = 1
        for note in list_note:
            if change_filter == note[x] in note:
                index = list_note.index(note)
                print(i, ". ", list_note[index])
                index_list.append(index)
                i = i+1
            

        # print(index_list)
        if len(index_list) == 1:
            ls= ex.input_data()
            print(f'Заметка {list_note[index]} успешно изменина. \nНа {ls}')
            list_note.pop(index)
            list_note.insert(index, ls)
            imp.rewrite_csv(list_note, path, 'w')
            return
        elif len(index_list) > 1:
            i = ex.digit(len(index_list))
            ls= ex.input_data()
            print(f'Заметка {list_note[index_list[i-1]]} успешно изменина. \nНа {ls}')
            list_note.pop(index)
            list_note.insert(index, ls)
            imp.rewrite_csv(list_note, path, 'w')
            return
        else:
            print('По этим данным "{}" заметка не найден.'.format(change_filter))

    # удаление заметки
    def delete_note(path, x):
        index_list = []
        list_note = exp.read_data(path)
        # print('Введите параметры поиска: ')
        delete_filter = ex.check_input_string('ваши параметры')
        i = 1
        for note in list_note:
            if delete_filter == note[x] in note:
                index = list_note.index(note)
                print(i, ". ", list_note[index])
                index_list.append(index)
                i = i+1

        # print(index_list)
        if len(index_list) == 1:
            print(f'Заметка {list_note[index]} успешно удалёна.')
            list_note.pop(index)
            imp.rewrite_csv(list_note, path, 'w')
            return
        elif len(index_list) > 1:
            i = ex.digit(len(index_list))
            print(f'Заметка {list_note[index_list[i-1]]} успешно удалёна.')
            list_note.pop(index_list[i-1])
            imp.rewrite_csv(list_note, path, 'w')
            return
        else:
            print('По этим данным "{}" заметка не найден.'.format(delete_filter))
