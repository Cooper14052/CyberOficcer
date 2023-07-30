import pyfiglet
import time

logo = pyfiglet.figlet_format('Cyber_Officer')
print(logo)

hosts = r'C:\Windows\System32\drivers\etc\hosts'

redirect_url = '127.0.0.1'
print("""Copyright (c) 2023 Киберагенты ИБ
Разработчики: Ястремской А.А.
              Стасюк В.Л.            
Программное обеспечение предназначено для защиты пользователей от утечки конфиденциональной информации.
Утилита напрямую работает с конфигурационными файлами системы пользователя. Запуск следует производить
с максимальным уровнем доступа или root.
""")
time.sleep(2)
print('Загрузка Базы данных.....')
try:
    with open('block_list', 'r') as bl:
        while True:
            block_element = bl.readline()
            with open('hosts.txt', 'r+') as file:
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

input()

