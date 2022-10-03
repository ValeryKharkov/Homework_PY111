"""
Считалочка.
Дано N человек, считалка из K слогов.
Считалка начинает считать с первого человека.
Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
Игра происходит до тех пор, пока не останется последний человек.
Для данных N и К дать номер последнего оставшегося человека.
"""


def leave(n_human: list, k_number: int):
    ind = 0

    while len(n_human) != 1:
        for _ in range(k_number):
            if ind == len(n_human):
                ind = 0
            ind += 1
        ind -= 1
        n_human.pop(ind)

    return n[0]


def number_remaining_human(n_human):
    pass


if __name__ == "__main__":
    n = ['Коля', 'Вася', 'Дима', 'Аня', 'Олег', 'Таня']
    n_copy = n.copy()
    k = 4

    print('Остался:',leave(n, k))

    print('Номер оставшегося:', n_copy.index(leave(n, k)) + 1)
