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


def place_items(items:list[dict]) -> list[list]:
    backpack = [['','',''] for _ in range(3)]
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


def main():
    items = read_file('items.txt')
    sorted_items = sorted(items, key = lambda item: (-item['Очки выживания'] / item['Размер'], item['Размер']))
    needed_items = get_needed_items(sorted_items=sorted_items)
    other_items = [item for item in sorted_items if item not in needed_items]
    needed_items.sort(key=lambda item: -item['Размер'])
    result = sum(item['Очки выживания'] for item in needed_items) - sum(item['Очки выживания'] for item in other_items)
    backpack = place_items(needed_items)
    # print()
    for line in backpack: print(line)
    print(f'очки выживания: {result}')

if __name__ == '__main__':
    main()