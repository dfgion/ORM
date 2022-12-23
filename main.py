from functions import main_functions as mf
import sqlalchemy

def main():
    start = True
    HELP="""
    /createdb - Создать структуру БД. Очищает данные, если они имеются.
    /autofill - Автозаполнение таблицы данными из json-файла
    /info - Выводит всю информацию о покупке книг определенного издателя
    
            """
    print('Для справки введите /help')
    while start:
        command = input('Введите команду:\n')
        if command == '/help':
            print(HELP)
        elif command == '/createdb':
            function_tool.create_db()
        elif command == '/autofill':
            function_tool.autofill_db_data()
        elif command == '/exit':
            return 'Завершение работы'
        elif command == '/help':
            print(HELP)
        elif command == '/info':
            setting = input('Выполнить поиск по id или имени? Id/Имя\n').lower()
            if setting == 'id':
                id = int(input('Введите id:\n'))
                function_tool.info_book(criteria=id)
            elif setting == 'имя':
                name_author = input('Введите имя:\n')
                function_tool.info_book(criteria=name_author)
        else:
            print('Неизвестная команда. Введите /help для справки по командам')
if __name__ == '__main__':
    DB = input('Введите название программы БД:\n').lower()
    DBname = input('Введите название вашей БД:\n')
    User = input('Введите имя пользователя, от которого хотите подключиться:\n')
    Password = input('Введите пароль пользователя, от которого подключаетесь:\n')
    setting_port = input('Порт по умолчанию 5432, хотите поменять? Да/Нет\n')
    if setting_port.lower() == 'да':
        port = int(input('Введите порт'))
        DSN = f'{DB}://{User}:{Password}@localhost:{port}/' + DBname
    elif setting_port.lower() == 'нет':
        DSN = f'{DB}://{User}:{Password}@localhost:5432/' + DBname
    else:
        DSN = f'{DB}://{User}:{Password}@localhost:5432/' + DBname
        print('Некорректный ответ, порт задан по умолчанию')
    engine = sqlalchemy.create_engine(DSN)
    function_tool = mf(engine=engine)
    main()






    