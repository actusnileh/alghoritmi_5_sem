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
        steps = []  # Список для записи шагов
        result, steps = IterMatrixService._optimal_parens_recursive(k, i, j, steps)
        return result, steps

    @staticmethod
    def _optimal_parens_recursive(k, i, j, steps) -> tuple[str, list[str]]:
        if i == j:
            # Если это единственная матрица, возвращаем её имя
            steps.append(
                f"Добавляем матрицу A{i+1} в результат, так как это единственная матрица.",
            )
            return f"A{i+1}", steps
        else:
            # Сначала добавляем открывающую скобку
            steps.append(
                f"Добавляем открывающую скобку для матриц с индексами i={i+1}, j={j+1}.",
            )

            # Рекурсивно строим левую часть выражения
            steps.append(
                f"Рекурсивно вызываем для левой части: i={i+1}, j={k[i][j]+1}.",
            )
            result_left, steps = IterMatrixService._optimal_parens_recursive(
                k,
                i,
                k[i][j],
                steps,
            )

            # Рекурсивно строим правую часть выражения
            steps.append(
                f"Рекурсивно вызываем для правой части: i={k[i][j]+2}, j={j+1}.",
            )
            result_right, steps = IterMatrixService._optimal_parens_recursive(
                k,
                k[i][j] + 1,
                j,
                steps,
            )

            # После рекурсивного вызова добавляем правую часть и закрывающую скобку
            result = f"({result_left} x {result_right})"
            steps.append(
                f"Добавляем закрывающую скобку для матриц с индексами i={i+1}, j={j+1}.",
            )
            steps.append(
                f"Получаем подвыражение: ({result_left} x {result_right}) для i={i+1}, j={j+1}.",
            )

            return result, steps
