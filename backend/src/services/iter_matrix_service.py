class IterMatrixService:

    @staticmethod
    def matrix_chain_order(p) -> tuple[list[list[int]], list[list[int]], list[str]]:
        n = (
            len(p) - 1
        )  # Количество матриц (на единицу меньше, чем количество элементов)
        matrix = [[0] * n for _ in range(n)]  # Таблица для минимальных стоимостей
        k = [[0] * n for _ in range(n)]  # Таблица для хранения индексов разбиений
        steps = []  # Список для записи шагов

        # Перебираем длины от 2 до n
        for length in range(2, n + 1):  # Длина цепочки от 2 до n
            for i in range(
                n - length + 1,
            ):  # Для каждой подцепочки длины `length` перебираем её начало (индекс i)
                j = i + length - 1  # Конец подцепочки
                matrix[i][j] = float("inf")  # Начинаем с бесконечности

                # Перебираем все возможные разбиения
                for s in range(i, j):  # Разбиение на две подцепочки
                    # Стоимость разбиения
                    cost = matrix[i][s] + matrix[s + 1][j] + p[i] * p[s + 1] * p[j + 1]

                    # Шаги для логирования
                    steps.append(
                        f"i={i+1}, j={j+1}, k={s+1}, m[{i+1},{s+1}] + m[{s+2},{j+1}] + p[{i}] * p[{s+1}] * p[{j+1}]",
                    )
                    steps.append(
                        f"Рассчитываем: {matrix[i][s]} + {matrix[s+1][j]} + {p[i]} * {p[s+1]} * {p[j+1]} = {cost}",
                    )

                    # Обновляем только если нашли меньшую стоимость
                    if cost < matrix[i][j]:
                        matrix[i][j] = cost
                        k[i][j] = s  # Сохраняем индекс разбиения
                        steps.append(
                            f"Обновляем минимальную стоимость для i={i+1}, j={j+1}, k={s+1}",
                        )

        # Возвращаем результат: минимальные стоимости, индексы разбиений и шаги
        return matrix, k, steps

    @staticmethod
    def optimal_parens(k, i, j) -> tuple[str, list[str]]:
        stack = [(i, j)]
        result = []
        steps = []  # Список для записи шагов

        while stack:
            i, j = stack.pop()

            if i == j:
                result.append(f"A{i+1}")
                steps.append(f"Добавляем матрицу A{i+1} в результат")
            else:
                result.append("(")
                steps.append(f"Добавляем открывающую скобку для i={i+1}, j={j+1}")

                stack.append((k[i][j] + 1, j))
                stack.append((i, k[i][j]))

        result.append(")")
        steps.append("Добавляем закрывающую скобку")
        return "".join(result), steps
