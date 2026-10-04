from time import time, sleep
from math import sqrt

def preparation():
    text_bg_colors = """Background Bright Black: \u001b[40;1m
Background Bright Red: \u001b[41;1m
Background Bright Green: \u001b[42;1m
Background Bright Yellow: \u001b[43;1m
Background Bright Blue: \u001b[44;1m
Background Bright Magenta: \u001b[45;1m
Background Bright Cyan: \u001b[46;1m
Background Bright White: \u001b[47;0m
Background Bright Grey: \u001b[47;1m"""
    global reset
    reset = "\u001b[0m"
    global bg_colors
    bg_colors = {}
    for line in text_bg_colors.split('\n'):
            name, color = line.split(': ')
            bg_colors[name] = color


def logic():
    print("Гузанов Максим, R1.3, вариант 10", end = '\n\n')

    preparation()

    dict_tasks = {1: Task1, 2: Task2, 3: Task3, 4: Task4, 5: Dop_task}
    ans = input('Вы хотите увидеть решение всех заданий? (Y/N) : ')
    while ans not in ['Y', 'N']:
        ans = input('Произошла ошибка, повторите попытку. Вы хотите увидеть решение всех заданий? (Y/N) : ').strip()
    if ans == 'Y':
        print()
        for i in dict_tasks:
            dict_tasks[i]()
    else:
        while True:
            tasks = input('Введите задания, решения которых вы хотите увидеть. Пример: "1,2,5" (Доп задание - 5). Задания: ')

            try:
                list_tasks = [int(x) for x in tasks.split(',')]
                break
            except:
                continue

        print()
        for task in list_tasks:
            dict_tasks[task]()


def get_bg_color(n:int, color:str):
        text_color = 'Background Bright ' + color
        return f'{bg_colors[text_color]}{" " * n}{reset}'


def decorator(func):
    def wrapper():
        print(func.__name__ + ': ')
        func()
        sleep(2)
        print()
    return wrapper

     
#вывести флаг Швейцарии
@decorator
def Task1():
    

    
    for i in range(10):
        if 0 <= i <= 1 or 8 <= i <= 9:
            print(f'{get_bg_color(20, 'Red')}{reset}')
        elif 2 <= i <= 3 or 6 <= i <= 7:
            print(f'{get_bg_color(8, 'Red')}{get_bg_color(4, 'White')}{get_bg_color(8, 'Red')}')
        else:
             print(f'{get_bg_color(3,'Red')}{get_bg_color(14, 'White')}{get_bg_color(3,'Red')}')
            

# сгенерировать повторяющийся узор
@decorator
def Task2():
    def draw_touching_circles():
        width = 80
        height = 28
        
        aspect_ratio = 2.0 

        radius = 14
        
        center_y = 20
        
        # Координаты X центров: первая в левой части, вторая сдвинута ровно на 2 радиуса вправо
        c1_x = 25
        c2_x = c1_x + (radius * 2)  # 25 + 24 = 49
        
        # Толщина линии окружности
        thickness = 1.5

        for y in range(13,height):
            line = ""
            for x in range(width):
                # Корректируем координату y под пропорции пикселя консоли
                adj_y = y * aspect_ratio
                adj_center_y = center_y * aspect_ratio
                
                # Расстояние от текущей точки до центра первой окружности
                dist1 = sqrt((x - c1_x) ** 2 + (adj_y - adj_center_y) ** 2)
                # Расстояние до центра второй окружности
                dist2 = sqrt((x - c2_x) ** 2 + (adj_y - adj_center_y) ** 2)
                
                # Проверяем попадание на границу окружностей
                is_circle1 = abs(dist1 - radius) < thickness
                is_circle2 = abs(dist2 - radius) < thickness
                
                if is_circle1 or is_circle2:
                    line += get_bg_color(1,'Grey')
                else:
                    line += " "
            print(line)

    start_time = time()
    while True:           
        draw_touching_circles()
        sleep(1)
        elapsed_time = time() - start_time
        if elapsed_time >= 3:
            print("Прошло 3 секунды")
            break


# анимация 3-4 кадра
@decorator
def Task3():
    start_time = time()
    flag = False
    while True:
        elapsed_time = time() - start_time
        if elapsed_time >= 3:
            flag = True

        m = ['/', '-', '\\', '|']
        for i in range(len(m)):
            if i == 3 and flag: e = "\n"
            else: e = "\r"
            print(f'[{m[i] * 30}]', flush=True, end = e)
            sleep(0.2)

        if flag: 
            print("Прошло 3 секунды")
            break

    num = int(input("Введите количество загрузок: "))
    for num_process in range(1, num + 1):
        width = 25
        for progress in range(0, width + 1):
            progress_bar = f'[{'#'*progress + '-'*(width - progress)}]'
            if num_process == num and progress == 25: e = '\n'
            else: e = '\r'
            print(f'Task_{num_process} ({num_process}/{num}) {progress_bar} {progress*4:>4}%', end = e, flush=True)
            sleep(0.1)
    print('Все загрузки успешно выполнены')



             
# диаграмма
@decorator
def Task4():
    m1,m2 = [], []
    for num in open('sequence.txt'):
        num = float(num)
        if -3 <= num <= 3:
            m1.append(num)
        else:
            m2.append(num)

    l1, l2, su = len(m1), len(m2), len(m1) + len(m2)
    print(f'len1 = {l1}, len2 = {l2}, sum = {su}')
    o1,o2 = l1/su*100, l2/su*100
    print(f'o1 = {o1}%, o2 = {o2}%')
    otn1, otn2 = int(o1/5), int(o2/5)
    print(f'[{'#'*otn1}{'-'*otn2}] {round(o1)}% / {round(o2)}% (o1 / o2)')
    print(f'{get_bg_color(otn1, 'Red')} - m1')
    print(f'{get_bg_color(otn2, 'Blue')} - m2')

# допзадание (график y = x/3)
@decorator
def Dop_task():
    width = 29
    height = 10
    matrix = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        x = 3 * y
        x1, x2 = x-1, x+1
        for i in [x, x1, x2]:
            matrix[height - 1 - y][i] = 1



    print('График y = x/3:')
    for row_index, row in enumerate(matrix):
        y = height - 1 - row_index
        axis = '+' if y == 0 else '|'
        line = ''.join(
            axis if x == 0 else
            '--' if y == 0 else
            get_bg_color(2, 'Grey') if pixel else '  '
            for x, pixel in enumerate(row)
        )
        print(f'{y:>2} {line}')

    x_labels = [' '] * (width * 2)
    for x in range(0, width, 3):
        label = str(x)
        x_labels[x * 2:x * 2 + len(label)] = label
    print('   ' + ''.join(x_labels))


if __name__ == '__main__':

    logic()
    

        
            