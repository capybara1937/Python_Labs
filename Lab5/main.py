import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'\t{func.__name__}:')
        func(*args, **kwargs, k=2)
    return wrapper


def main():
    dict_tasks = {
        1: task1,
        2: task2,
        3: task3,
        4: extra_task
    }
    ans = input('Вы хотите увидеть ответы на все задания? (y/n) ')
    if ans.lower() == 'y':
        for task in dict_tasks.values():
            task()
    else:
        task_number = int(input('Введите номер задания (1-4): '))
        if task_number in dict_tasks:
            dict_tasks[task_number]()
        else:
            print('Неверный номер задания. Пожалуйста, введите число от 1 до 4.')

@decorator
def task1(k:int = 1):
    file_path = "task1-ru.txt"
    data = read_file(file_path)
    reg1 = r'[a-zA-Z]+\.'
    reg2 = r'[0-9]+,[0-9]+'
    ans1 = re.findall(reg1, data)
    ans2 = re.findall(reg2, data)
    print(f"{'\t'*k}Слова после которых стоит точка: {ans1}")
    print(f"{'\t'*k}Числа с плавающей точкой: {ans2}")

@decorator
def task2(k:int = 1):
    file_path = "task2.html"
    data = read_file(file_path)
    reg = r'[0-9]+px'
    ans = re.findall(reg, data)
    print(f"{'\t'*k}Значения в пикселях: {ans}")

@decorator
def task3(k:int = 1):
    file_path = "task3.txt"
    data = read_file(file_path)
    data = data.split(' ')

    users = []
    user = {}
    for i in data:
        if re.fullmatch(r'[0-9]+', i):
            user['ID'] = int(i)
        elif re.fullmatch(r'[A-Z][a-z]+', i):
            user['Surname'] = i
        elif re.fullmatch(r'[A-Za-z0-9]+@[\w-]+\.\w+', i):
            user['Email'] = i
        elif re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', i):
            user['RegistrationDate'] = i
        else:
            user['Site'] = i

        if len(user) == 5:
            users.append(user)
            user = {}
            # print(f"{'\t'*k}Пользователь: {users[-1]}")
    with open('task3.csv', 'w', encoding='utf-8') as f:
        for user in users:
            f.write(f"{user['ID']},{user['Surname']},{user['Email']},{user['RegistrationDate']},{user['Site']}\n")
    print(f"{'\t'*k}Данные успешно записаны в файл task3.csv")
    print(f"{'\t'*k}Количество пользователей: {len(users)}")

@decorator
def extra_task(k:int = 1):
    file_path = "task_add.txt"
    data = read_file(file_path)

    re1 = r'[0-9]{4}[-/.]{1}[0-9]{2}[-/.]{1}[0-9]{2}'
    re2 = r'[0-9]{2}[-/.]{1}[0-9]{2}[-/.]{1}[0-9]{4}'
    ans1 = re.findall(fr'{re1}|{re2}', data)
    print(f"{'\t'*k}Найденные даты: {ans1}, количество: {len(ans1)}")

    reg2 = r'\w+@[a-z-]+\.[a-z]+'
    ans2 = re.findall(reg2, data)
    print(f"{'\t'*k}Найденные email адреса: {ans2}, количество: {len(ans2)}")

    reg3 = r'https?://[a-zA-Z0-9./-]+'
    ans3 = re.findall(reg3, data)
    print(f"{'\t'*k}Найденные URL: {ans3}, количество: {len(ans3)}")

if __name__ == "__main__":
    main()