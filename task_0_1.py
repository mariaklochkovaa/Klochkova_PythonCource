# Вариант 1
# Дана целочисленная прямоугольная матрица. Определить:
# 1) количество строк, не содержащих ни одного нулевого элемента;
# 2) максимальное из чисел, встречающихся в заданной матрице более одного раза.

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()


def count_rows_without_zero(matrix):
    count = 0  # лічильник для підрахунку рядків
    for row in matrix:  # проходимось по матриці
        is_zero = False
        for element in row:
            if element == 0:  # шукаемо елементи, які дорівнюють нулю
                is_zero = True
        if not is_zero:
            count += 1  # якщо в рядку немає нулів, збільшуємо лічильник на 1
    return count


def find_max_repeated_number(matrix):
    lst_repeated_numbers = []  # список для зберігання повторюваних елементів
    seen = []  # список для зберігання елементів матриці
    for row in matrix:
        for element in row:
            if element in seen:  # якщо елемент повторюється
                if element not in lst_repeated_numbers:  # і його ще немає в списку
                    lst_repeated_numbers.append(element)  # додаємо його до списку повторюваних
            else:
                seen.append(element)

    return max(lst_repeated_numbers)


def main():
    rows = int(input("Введіть кількість рядків: "))
    columns = int(input("Введіть кількість стовпців: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            element = int(input(f"Введіть елемент для [{i + 1},{j + 1}]: "))
            row.append(element)
        matrix.append(row)

    print("Матриця:")
    print_matrix(matrix)
    count = count_rows_without_zero(matrix)
    print(f"Кількість рядків без нуля: {count_rows_without_zero(matrix)}")
    print(
        f"Максимальне серед чисел, що зустрічаються у заданій матриці більше одного разу: {find_max_repeated_number(matrix)}")


if __name__ == "__main__":
    main()
