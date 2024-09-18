class IterMatrixService:

    @staticmethod
    def matrix_chain_order(p) -> tuple[list[list[int]], list[list[int]]]:
        n = len(p) - 1  # Количество матриц
        matrix = [[0] * n for _ in range(n)]  # Таблица для минимальных стоимостей
        k = [[0] * n for _ in range(n)]  # Таблица для хранения индексов разбиений

        # length - длина цепочки матриц
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                matrix[i][j] = float("inf")
                for s in range(i, j):
                    cost = matrix[i][s] + matrix[s + 1][j] + p[i] * p[s + 1] * p[j + 1]
                    if cost < matrix[i][j]:
                        matrix[i][j] = cost
                        k[i][j] = s  # Сохраняем индекс разбиения

        return matrix, k

    @staticmethod
    def optimal_parens(s, i, j) -> str:
        # Используем стек для обработки пар индексов и знака открытия/закрытия
        stack = [(i, j, False)]  # Последний элемент в кортеже - открывать ли скобку
        result = []

        while stack:
            i, j, to_open = stack.pop()

            if i == j:
                result.append(
                    f"A{i + 1}",
                )  # Добавляем матрицу A(i+1), т.к. индексация с 0
            else:
                if not to_open:
                    # Добавляем текущий блок скобок и раскладываем его на подзадачи
                    result.append("(")
                    stack.append((i, j, True))  # Для закрытия после рекурсивных вызовов
                    stack.append((s[i][j] + 1, j, False))  # Правая часть цепочки
                    stack.append((i, s[i][j], False))  # Левая часть цепочки
                else:
                    result.append(")")

        return "".join(result)
