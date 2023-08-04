import time
import sys
from tkinter import *
from tkinter import ttk

hosts = r'C:\Windows\System32\drivers\etc\hosts'
redirect_url = '127.0.0.1'

def doc_info():
    print('Docum')
def start_programm():
    print("""Copyright (c) 2023 КиберАгенты ИБ
    Разработчики: Ястремской А.А.
                  Стасюк В.Л.            
    Программное обеспечение предназначено для защиты пользователей от утечки конфиденциональной информации.
    Утилита напрямую работает с конфигурационными файлами системы пользователя. Запуск следует производить
    с максимальным уровнем доступа или root.""")
    time.sleep(2)
    print('Загрузка Базы данных.....')
    try:
        with open('block_list', 'r') as bl:
            while True:
                block_element = bl.readline()
                with open(hosts, 'a') as file:
                    src = file.read()
                    if block_element in src:
                        pass
                    else:
                        file.write(f'{redirect_url} {block_element}')
                if not block_element:
                    break
        print('Работа утилиты завершена успешно!')
    except FileNotFoundError:
        print('[Warning] База данных не найдена.....')
    except PermissionError:
        print('[Warning] У вас нет прав на запуск данного элемента.....')

def exit():
    sys.exit('Завершение')



def window():
    window = Tk()
    window.title('SaveClick')
    window['bg'] = '#fafafa'
    window.geometry('300x250')
    window.wm_attributes('-alpha', 0.9)

    info_butt = Button(text='Documentation', command=doc_info)
    info_butt.place(x=10, y=200)

    start_butt = Button(text='Start', command=start_programm)
    start_butt.place(x=120, y=200)

    exit_butt = Button(text='Exit', command=exit)
    exit_butt.place(x=170, y=200)

    window.mainloop()


if __name__ == '__main__':
    window()
