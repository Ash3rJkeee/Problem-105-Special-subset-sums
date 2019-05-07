import itertools
import datetime


def conditional_test(many):
    """На вход принимает список. Возвращает результат проверки множества, соответствующего данному списку на условие
    задачи."""
    combinations = set()

    # создаем множество всех возможных подмножеств
    for i in range(1, len(many)):
        combinations.update(itertools.combinations(many, i))

    # преобразуем в список и сортируем для удобства печати при необходимости
    combinations = list(combinations)
    combinations.sort()

    # перебираем все возможные пары подмножеств для сравнения между собой
    for i in combinations:
        b_ = list(combinations)
        b_.remove(i)
        for j in b_:
            sum_i = sum(i)
            sum_j = sum(j)
            len_set_i = len(list(i))
            len_set_j = len(list(j))

            set_i = set(i)
            set_j = set(j)

            # определяем непересекающиеся подмножества и проводим над ними проверку по условию
            if set_i.isdisjoint(set_j):
                if sum_i == sum_j:
                    return False
                if len_set_i > len_set_j:
                    if sum_i <= sum_j:
                        return False
                if len_set_i < len_set_j:
                    if sum_i >= sum_j:
                        return False
    return True


f = open("p105_sets.txt", "r")

s = 0
n = 0
k = 0

start = datetime.datetime.now()


for line in f:
    line = line.strip()
    list_line = line.split(",")

    for i in range(len(list_line)):
        list_line[i] = int(list_line[i])

    n = n + 1
    test = conditional_test(list_line)
    if test:
        k = k + 1
        s = s + sum(list_line)

    print(n, list_line, "; test =", test,  "; sum =", s)

stop = datetime.datetime.now()
ellapsed_time = stop - start

print()
print("Вычисления закончены и заняли", ellapsed_time.seconds, "секунд.")
print("Всего просмотрено ", n, "строк. Из них подходят ", k, "Сумма = ", s)

f.close()

# Вычисления закончены и заняли 193 секунд.
# Всего просмотрено  100 строк. Из них подходят  28 Сумма =  73702