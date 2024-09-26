class LCSService:
    @classmethod
    def lcs_table(cls, s1, s2):
        len1, len2 = len(s1), len(s2)

        table = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    table[i][j] = (
                        table[i - 1][j - 1] + 1
                    )  # Если символы совпадают, то наша длина увелич. на 1, берем значения из верхней левой ячейки
                else:
                    table[i][j] = max(
                        table[i - 1][j],
                        table[i][j - 1],
                    )  # Если символы не совпадают, то берем максимальное значение из двух возможных вариантов

        return table

    @classmethod
    def lcs_recursive(cls, s1, s2, len1=None, len2=None):
        if len1 is None or len2 is None:
            len1, len2 = len(s1), len(s2)

        if len1 == 0 or len2 == 0:
            return 0

        # Если последний символ строк совпадает, увеличиваем счетчик
        if s1[len1 - 1] == s2[len2 - 1]:
            return 1 + cls.lcs_recursive(s1, s2, len1 - 1, len2 - 1)
        else:
            # Если символы не совпадают, проверяем оба варианта: убираем последний символ из s1 или s2
            return max(
                cls.lcs_recursive(s1, s2, len1 - 1, len2),
                cls.lcs_recursive(s1, s2, len1, len2 - 1),
            )
