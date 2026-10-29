from main import place_items, read_file
from itertools import combinations


def get_score(comb:list[dict], items:list[dict], points:int=10):
    untaken_items = [item for item in items if item not in comb]
    sum_1 = sum(item['Очки выживания'] for item in comb)
    sum_2 = sum(item['Очки выживания'] for item in untaken_items)
    score = points + sum_1 - sum_2
    
    # print()
    # for item in comb: print(item)
    # print(sum_1, sum(item['Размер'] for item in comb))
    # print()
    # for item in untaken_items: print(item)
    # print(sum_2)
    # print(f'{score} = {points} + {sum_1} - {sum_2}')

    return score


def get_combinations(items:list[dict], disease:str, hp:int, length:int, height:int):
    capacity = length * height
    res = []
    # print(capacity)
    for number_of_items in range(len(items)+1):
        for taken_items in combinations(items, number_of_items):
            taken_items = list(taken_items)
            untaken_items = [item for item in items if item not in taken_items]

            if disease == 'астма' and all(item['Обозначение'] != 'i' for item in taken_items):
                continue
            elif disease == 'паранойя' and all(item['Обозначение'] != 'd' for item in taken_items):
                continue

            if any(item['Размер'] > max(length, height) for item in taken_items):
                continue
            if sum(item['Размер'] for item in taken_items) <= capacity:
                points = hp + sum(item['Очки выживания'] for item in taken_items) - sum(item['Очки выживания'] for item in untaken_items)
                if points > 0:
                    res.append((taken_items, points))
    return res


def extra_task1(items:list[dict]):
    print()
    print('Решения для рюкзака с 7 ячейками')
    length, height, disease = 7, 1, 'нет'
    for hp in range(10,20+1,5):
        combs = get_combinations(items, disease, hp, length, height)
        print(f'Для hp = {hp}, {len(combs)} комбинаций, удовлетворяющих условию задачи')




if __name__ == "__main__":
    length, height, hp, disease = 3, 3, 10, 'нет' # length >= height
    items = read_file("items.txt")
    combs = get_combinations(items, disease, hp, length, height)

    combs.sort(key=lambda comb:-comb[1])
    best_comb, score = combs[0]
    backpack = place_items(best_comb, length, height)

    print(f'Для 10 варианта: очки выживания = {hp}, болезнь = {disease}, ячейки = {length}x{height}:')
    print(f'Найдено {len(combs)} комбинаций, удовлетворяющих условию задачи (счет > 0)')
    print(f'Лучшая комбинация: ')
    for line in backpack: print(line)
    print(f'Итоговый счёт: {score}')

    extra_task1(items)


