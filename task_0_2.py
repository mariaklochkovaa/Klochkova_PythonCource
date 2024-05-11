# Вариант 12
# Уплотнить заданную матрицу, удаляя из нее строки и столбцы, заполненные нулями. Найти номер
# первой из строк, содержащих хотя бы один положительный элемент.

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()


def delete_row(matrix, row):
    del matrix[row]


def delete_column(matrix, column):
    for row in matrix:
        del row[column]


def compact_matrix(matrix):
    lst_del_row = []  # список для зберігання рядків на видалення
    for i, row in enumerate(matrix):
        is_not_zero = False
        for element in row:
            if element > 0 or element < 0:  # перевіряємо, чи є в рядку числа, окрім від нуля
                is_not_zero = True
                break
        if not is_not_zero:  # якщо ні, додаємо до до списку на видалення
            lst_del_row.append(i)

    for i in lst_del_row:  # видаляємо рядки
        delete_row(matrix, i)

    num_columns = len(matrix[0]) - 1  # знаходимо кількість стовбців
    for i in range(num_columns, -1, -1):
        col_is_zero = all(row[i] == 0 for row in matrix)  # перевіряємо, чи всі елементи стовбця є нулями
        if col_is_zero:  # якщо так, видаляемо
            delete_column(matrix, i)


def positive(matrix):
    index_row_positive_number = None
    for i, row in enumerate(matrix):
        for element in row:  # шукаємо позитивний елемент
            if element > 0:
                index_row_positive_number = i + 1
                return index_row_positive_number  # повертаємо його рядок
    return print('Немає позитивних значень')


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
    compact_matrix(matrix)
    print('Матриця без рядків та стовбців з нулями:')
    print_matrix(matrix)
    print(f'Номер першого з рядків, що містять хоча б один додатній елемент:{positive(matrix)}')


if __name__ == "__main__":
    main()
