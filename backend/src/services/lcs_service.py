class LCSService:
    @classmethod
    def lcs_table(cls, s1, s2):
        len1, len2 = len(s1), len(s2)

        # Создаем таблицы для значений LCS и для направлений
        table = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        directions = [["o"] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                    directions[i][
                        j
                    ] = "↖"  # Символы совпадают, значит пришли с диагонали
                else:
                    if table[i - 1][j] >= table[i][j - 1]:
                        table[i][j] = table[i - 1][j]
                        directions[i][j] = "↑"  # Максимум пришел сверху
                    else:
                        table[i][j] = table[i][j - 1]
                        directions[i][j] = "←"  # Максимум пришел слева

        return table, directions

    @classmethod
    def find_all_lcs(cls, dp, X, Y, m, n):
        if m == 0 or n == 0:
            return {""}
        elif X[m - 1] == Y[n - 1]:
            lcs_set = LCSService.find_all_lcs(dp, X, Y, m - 1, n - 1)
            return {lcs + X[m - 1] for lcs in lcs_set}
        else:
            lcs_set = set()
            if dp[m - 1][n] >= dp[m][n - 1]:
                lcs_set.update(LCSService.find_all_lcs(dp, X, Y, m - 1, n))
            if dp[m][n - 1] >= dp[m - 1][n]:
                lcs_set.update(LCSService.find_all_lcs(dp, X, Y, m, n - 1))
            return lcs_set

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
