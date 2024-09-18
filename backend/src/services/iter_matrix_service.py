class IterMatrixService:

    @staticmethod
    def matrix_chain_order(p) -> tuple[list[list[int]], list[list[int]]]:
        n = len(p) - 1  # Количество матриц
        m = [[0] * n for _ in range(n)]  # Таблица для минимальных стоимостей
        s = [[0] * n for _ in range(n)]  # Таблица для хранения индексов разбиений

        # length - длина цепочки матриц
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                m[i][j] = float("inf")
                for k in range(i, j):
                    cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                    if cost < m[i][j]:
                        m[i][j] = cost
                        s[i][j] = k  # Сохраняем индекс разбиения

        return m, s

    @staticmethod
    def print_optimal_parens(s, i, j) -> None:
        if i == j:
            print(f"A{i+1}", end="")  # Выводим матрицу A(i+1), т.к. индексация с 0
        else:
            print("(", end="")
            IterMatrixService.print_optimal_parens(s, i, s[i][j])
            IterMatrixService.print_optimal_parens(s, s[i][j] + 1, j)
            print(")", end="")


p = [30, 35, 15, 5, 10, 20]
m, k = IterMatrixService.matrix_chain_order(p)

print(f"Минимальное количество операций: {m}")

print("Оптимальный порядок умножения: ", end="")
IterMatrixService.print_optimal_parens(k, 0, len(p) - 2)
print()
