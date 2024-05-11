# Вариант 15
# Дана целочисленная прямоугольная матрица. Определить номер первого из столбцов, содержащих
# хотя бы один нулевой элемент.
# Характеристикой строки целочисленной матрицы назовем сумму ее отрицательных четных
# элементов. Переставляя строки заданной матрицы, располагать их в соответствии с убыванием
# характеристик.

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()


def sum_negative_even_elements(row):  # функція для пошуку суми від'ємних парних елементів рядка (характеристика рядка)
    result = 0
    for element in row:
        if element < 0 and element % 2 == 0:
            result += element
    return result


def sort_matrix(matrix):  # сортуємо рядки відповідно до характеристик(від більшого к меньшому)
    sorted_matrix = sorted(matrix, key=lambda row: sum_negative_even_elements(row), reverse=True)
    return sorted_matrix


def find_first_zero_col(matrix):
    num_columns = len(matrix[0])
    for col in range(num_columns):
        for row in matrix:  # шукаємо елемент, який дорівнює нулю
            if row[col] == 0:
                return col + 1  # повертаємо його стовбець
    return print('У матриці немає нулів')


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
    print(f'Номер першого зі стовпців, що містять хоча б один нульовий елемент:{find_first_zero_col(matrix)}')
    matrix = sort_matrix(matrix)
    print('Матриця, відсортована за спаданням харакеристик:')
    print_matrix(matrix)


if __name__ == "__main__":
    main()
