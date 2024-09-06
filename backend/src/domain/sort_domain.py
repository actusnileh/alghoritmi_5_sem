class SortMethods:
    @staticmethod
    def SortDirectInclusion(massive: list[int]) -> list[int]:
        """Сортировка с помощью прямого включения"""
        size = len(massive)
        for i in range(1, size):
            x = massive[i]
            j = i - 1
            while j >= 0 and x < massive[j]:
                massive[j + 1] = massive[j]
                j -= 1
            massive[j + 1] = x
        return massive

    @staticmethod
    def SortDirectSelection(massive: list[int]) -> list[int]:
        """Сортировка с помощью прямого выбора"""
        size = len(massive)
        for i in range(1, size - 1):
            x = massive[i]
            k = i
            for j in range(i + 1, size):
                if massive[j] < x:
                    k = j
                    x = massive[j]
            massive[k] = massive[i]
            massive[i] = x
        return massive

    @staticmethod
    def SortDirectExchange(massive: list[int]) -> list[int]:
        """Сортировка с помощью прямого обмена"""
        size = len(massive)
        for i in range(2, size):
            for j in range(size - 1, i - 1, -1):
                if massive[j - 1] > massive[j]:
                    massive[j - 1], massive[j] = massive[j], massive[j - 1]
        return massive

    @staticmethod
    def QuickSort(massive: list[int]) -> list[int]:
        """Метод быстрой сортировки"""
        if len(massive) <= 1:
            return massive
        pivot = massive[len(massive) // 2]
        left = [x for x in massive if x < pivot]
        middle = [x for x in massive if x == pivot]
        right = [x for x in massive if x > pivot]
        return SortMethods.QuickSort(left) + middle + SortMethods.QuickSort(right)

    @staticmethod
    def ShellSort(massive: list[int]) -> list[int]:
        """Метод Шелла"""
        size = len(massive)
        interval = size // 2
        while interval > 0:
            for i in range(interval, size):
                temp = massive[i]
                j = i
                while j >= interval and massive[j - interval] > temp:
                    massive[j] = massive[j - interval]
                    j -= interval
                massive[j] = temp
            interval //= 2
        return massive
