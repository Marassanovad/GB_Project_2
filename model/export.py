import csv
from excep import Excep as ex
from interface import user_interface as console


def read_data(path): #Функция, читает данные из файла в список
    
    ex.read_file_except(path)
    with open(path, "r") as file:
        reader = csv.reader(file)
        data_list = []
        for row in reader:
            data_list.append(row)
        return data_list
			

def show_all_notes(path): #Функция, выводит все заметки из указанного .csv файла.

	list_note = read_data(path)
	
	print('''\t ID ||   Дата   ||   Заголовок  ''')
	print('=' * 50)
	for note in list_note:
		print(f'\t {note[0]}. || {note[1]} ||   {note[2]} \n       Заметка: {note[3]}' )
	print('=' * 50)


def selected_filter(path):
    while (True):
        console.Interface("Notes_Search")
        k = ex.action()
        if k == "1":  
            print('-'*50)
            print('Вы выбрали "По идентификатору"')
            print('-'*50)
            show_selected_note(path, 0)

        elif k == "2": 
            print('-'*50)
            print('Вы выбрали "По заголовоку"')
            print('-'*50)
            show_selected_note(path, 2)
                    
        elif k == "3": 
            print('-'*50)
            print('Вы выбрали "По дате"')
            print('-'*50)
            show_selected_note(path, 1)        

        elif k == "4":
            print('-'*50)
            print("Производиться выход в главное меню")
            print('-'*50)
            break
                     
        else:
            print('-'*50)
            print("Вы ввели неправильные данные")
            print('-'*50)


#доделать
def show_selected_note(path, x):
	'''
	Функция, выводит информацию о заметках по указанным данным
	'''

	list_note = read_data(path)
	print('Введите параметры поиска: ')
	search_filter = ex.check_input_string('Ваши данные')
	
	for note in list_note:
		if search_filter == note[x] in note:
			index = list_note.index(note)
			print(list_note[index])
           
	# print('По этим данным "{}" заметка не найден.'.format(search_filter))
