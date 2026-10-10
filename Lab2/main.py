from os import listdir, remove
import xml.etree.ElementTree as ET


def logic():

    def ask_all():
        ans = input("Вы хотите увидеть результат всех заданий? (y/n): ")
        if ans not in ['y', 'n']:
            print('Извините, я вас не понял. Попробуйте еще раз.')
            return logic(books)
        return ans == 'y'
    

    def ask_for_tasks():
        ans1 = input('Какие задания вы хотите увидеть? (1,2,3,4): ')
        try:
            ans1 = [int(x) for x in ans1.split(',')]
        except Exception as e:
            print(f'Извините, я вас не понял. Произошла ошибка: {e}. Попробуйте еще раз.')
            return ask_for_tasks()
        return ans1

    books = read_file()
    dict = {1: (task1, [books]), 2: (task2, [books]), 3: (task3, [books]), 4: (task4, [])}
    res = ask_all()
    if res:
        for task, args in dict.values():
            task(*args)
    else:
        tasks = ask_for_tasks()
        for task in tasks:
            func, args = dict[task][0], dict[task][1]
            func(*args)


def read_file(file_name:str = 'books.csv') -> list:
    file = open(file_name, 'r')
    names = file.readline().strip().split(';')
    # print(names)
    books = []
    for line in file:
        line = line.strip().split(';')
        book = dict(zip(names, line))
        books.append(book)
    file.close()
    return books


def task1(books:list[dict]):
    ans1 = len([book for book in books if len(book['Название']) > 30])
    print(f'ans1 = {ans1}')


def search_by_author(books:list[dict], author:str) -> list[dict]:
    needed_books = []
    for book in books:
        if book['Автор'] == author:
            # year = int(book['Дата поступления'].split(' ')[0].split('.')[-1])
            # if year >= 2018:
            needed_books.append(book)
    return needed_books


def task2(books:list[dict]):
    authors = []
    for book in books:
        if book['Автор'] in authors: continue
        year = book['Дата поступления'].split(' ')[0].split('.')[-1]
        if year == 'Лукьяненко': # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            continue
        year = int(year)
        if year >= 2018:
            authors.append(book['Автор'])
    
    author = input(f'Авторы: {', '.join(authors[:3])}. Книги какого автора вы бы хотели найти: ')
    while author not in authors:
        author = input('Извините у нас нет книг этого автора. Книги какого автора вы бы хотели найти: ')
    needed_books = search_by_author(books, author)
    print(f'Вот примеры книг, автор которых - {author}:')
    for ind_book in range(min(2, len(needed_books))):
        print(f'{ind_book+1:>4}) {needed_books[ind_book]}', end='\n\n')


def get_link(book:dict) -> dict:
    names = ['Автор', 'Название', 'год']
    link = {}
    for name in names:
        if name == 'год':
            link[name] = int(book['Дата поступления'].split(' ')[0].split('.')[-1])
        else: link[name] = book[name]
    return link


def task3(books:list[dict], file_name:str = 'task3.txt'):
    links = []
    for ind in range(0, len(books), len(books)//20):
        link = get_link(books[ind])
        text = f'<{link['Автор']}>. <{link['Название']}> - <{link['год']}>'
        links.append(text)

    if file_name in listdir():
        remove(file_name)
        print(f'{file_name} deleted')

    with open(file_name, 'x') as file:
        file.write('\n'.join(links))

    print(f'Файл {file_name} успешно создан. В нем {len(links)} ссылок на книги.')


def task4(file_name:str = 'currency.xml'):
    if file_name not in listdir():
        print(f'Файл {file_name} не найден.')
        return

    tree = ET.parse(file_name)
    root = tree.getroot() 
    CharCodes = []
    Names = []
    for child in root:
        for sub_child in child:
            if sub_child.tag == 'CharCode':
                CharCodes.append(sub_child.text)
            elif sub_child.tag == 'Name':
                Names.append(sub_child.text)
    result = dict(zip(CharCodes, Names))
    print(f'Вот список валют, которые есть в файле {file_name}:')
    for char_code, name in result.items():
        print(f'  {char_code}: {name}')



if __name__ == "__main__":
    logic()