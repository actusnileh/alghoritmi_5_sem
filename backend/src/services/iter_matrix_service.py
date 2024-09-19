class IterMatrixService:

    @staticmethod
    def matrix_chain_order(p) -> tuple[list[list[int]], list[list[int]]]:
        n = len(p) - 1  # Количество матриц (На единицу меньше, чем кол-во элементов)
        matrix = [[0] * n for _ in range(n)]  # Таблица для минимальных стоимостей
        k = [[0] * n for _ in range(n)]  # Таблица для хранения индексов разбиений

        for length in range(
            2,
            n + 1,
        ):  # Перебираем длины от 2 до n (длину 1 не учитываем, так как это одна матрица)
            for i in range(
                n - length + 1,
            ):  # Для каждой подцепочки длины `length` перебираем её начало (индекс i)
                j = i + length - 1  # конец подцепочки
                matrix[i][j] = float("inf")
                for s in range(i, j):
                    cost = (
                        matrix[i][s] + matrix[s + 1][j] + p[i] * p[s + 1] * p[j + 1]
                    )  # Вычисляем стоимость разбиения цепочки по формуле (от i до s и от s+1 до j)
                    if (
                        cost < matrix[i][j]
                    ):  # Если текущая стоимость меньше, чем уже сохранённая, обновляем её
                        matrix[i][j] = cost
                        k[i][j] = s  # Сохраняем индекс

        return matrix, k

    @staticmethod
    def optimal_parens(s, i, j) -> str:
        # Стек для обработки пар индексов (i, j) и информации о скобке
        stack = [(i, j, False)]
        result = []

        while stack:
            i, j, to_open = (
                stack.pop()
            )  # Извлекаем пару индексов и флаг открывающей/закрывающей скобки

            if i == j:  # Если это одна матрица, добавляем её
                result.append(
                    f"A{i + 1}",
                )
            else:
                if not to_open:
                    # Добавляем открывающую скобку и подзадачи для подцепочек
                    result.append("(")
                    # Добавляем задачу для закрытия скобки
                    stack.append((i, j, True))
                    # Добавляем задачи для правой и левой частей цепочки
                    stack.append((s[i][j] + 1, j, False))  # Правая часть цепочки
                    stack.append((i, s[i][j], False))  # Левая часть цепочки
                else:
                    # Если дошли до конца цепочки, добавляем закрывающую скобку
                    result.append(")")

        return "".join(result)
