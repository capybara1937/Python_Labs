from csv import DictReader

def read_file(file_path) -> list[dict]:
    list = []
    with open(file_path, mode = 'r', encoding = 'utf-8') as file:
        reader = DictReader(file, delimiter = '\t')
        for row in reader:
            row['Размер'] = int(row['Размер'].split(' ')[0])
            if '*' in row['Очки выживания']:
                row['Очки выживания'] = row['Очки выживания'].replace('*', '')
            row['Очки выживания'] = int(row['Очки выживания'])
            list.append(row)
    return list


def get_needed_items(sorted_items:list[dict], capacity:int = 9, width:int = 3, height:int = 3) -> list[dict]:
    needed_items = []
    # for line in backpack: print(line)
    capacity = 9
    # for item in sorted_items: print(item)
    # print()

    for item in sorted_items:
        if capacity - item['Размер'] >= 0 and item['Размер'] <= max(width, height):
            needed_items.append(item)
            capacity -= item['Размер']
            # print(' '.join([item['Предмет'] for item in sorted_items]))
            # print(f'Взял: {' '.join([f'{key} - {str(item[key])};' for key in ['Предмет', 'Размер', 'Очки выживания']])} {capacity}')
        else: continue
    return needed_items


def place_items(items:list[dict], w:int = 3, h:int = 3) -> list[list]:
    backpack = [['' for _ in range(w)] for _ in range(h)]
    items.sort(key = lambda item: -item['Размер'])
    # for item in items: print(item)
    # print()
    for item in items:
        # print(item)
        for ind_line in range(len(backpack)):
            line = backpack[ind_line]
            capacity_line = line.count('')
            if capacity_line >= item['Размер']:
                # print(f'подходит {ind_line} capacity - {capacity_line} для {item['Предмет']}')
                for _ in range(item['Размер']):
                    for ind_place in range(len(line)):
                        if line[ind_place] != '': continue
                        line[ind_place] = item['Обозначение']
                        # print(item['Обозначение'], backpack)
                        break
                break
            # else:
                print(f'line {ind_line} не подходит для {item['Предмет']} т. к. {item['Размер']} > {capacity_line}')
        # print()
    return backpack


def get_best_combination():
    items = read_file('items.txt')
    sorted_items = sorted(items, key = lambda item: (-item['Очки выживания'] / item['Размер'], item['Размер']))
    needed_items = get_needed_items(sorted_items=sorted_items)
    other_items = [item for item in sorted_items if item not in needed_items]
    needed_items.sort(key=lambda item: -item['Размер'])
    result = sum(item['Очки выживания'] for item in needed_items) - sum(item['Очки выживания'] for item in other_items)
    backpack = place_items(needed_items, 3, 3)
    # print()
    for line in backpack: print(line)
    print(f'очки выживания: {result}')


def get_memo_table(items:list[dict], A:int)->list[list[int]]:
    weights = [item['Размер'] for item in items]
    values = [item['Очки выживания'] for item in items]
    table = [[0 for _ in range(A + 1)] for _ in range(len(weights) + 1)]

    for row_ind in range(1,len(weights) + 1):  # row_ind = кол-во первых исп. предметов [1, 12]            
        for col_ind in range(1, A + 1):        # col_ind = вместимость текущего рюкзака [1, 9]
            item_ind = row_ind - 1
            weight = weights[item_ind]
            value = values[item_ind]

            if weight <= col_ind:
                table[row_ind][col_ind] = value + table[row_ind-1][col_ind - weight]
            else:
                table[row_ind][col_ind] = table[row_ind-1][col_ind]
    return table
            

def get_used_items(table:list[list[int]], items:list[dict], A:int)-> list[dict]:
    used_items = []
    row_ind = len(items)
    col_ind = A
    value = table[row_ind][col_ind]
    while value > 0:
        item_ind = row_ind - 1
        if value == table[row_ind-1][col_ind]: # предмет не использовался
            row_ind -= 1
        else:
            used_items.append(items[item_ind])
            row_ind -= 1
            col_ind -= items[item_ind]['Размер']
            value = table[row_ind][col_ind]
    return used_items


def get_combination_by_memotable():
    items = read_file('items.txt')
    table = get_memo_table(items, 9)
    # for i in table: print(i)
    used_items = get_used_items(table, items, 9)
    unused_items = [item for item in items if item not in used_items]
    print('использованные предметы')
    for item in used_items: print(item)
    print('неиспользованные предметы')
    for item in unused_items: print(item)
    result = sum(item['Очки выживания'] for item in used_items) - sum(item['Очки выживания'] for item in unused_items)
    backpack = place_items(used_items, 3, 3)
    for line in backpack: print(line)
    print(f'Очки выживания: {result}')



if __name__ == '__main__':
    get_best_combination()
    # get_combination_by_memotable()