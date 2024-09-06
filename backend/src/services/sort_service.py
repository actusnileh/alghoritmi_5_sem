import random
import time
from typing import Callable

from src.domain.sort_domain import SortMethods
from src.schema.sort_schema import (
    TimingSort,
    TimingsSort,
)


class SortingService:
    def __init__(self):
        self.sort_methods = {
            "SortDirectInclusion": SortMethods.SortDirectInclusion,
            "SortDirectSelection": SortMethods.SortDirectSelection,
            "SortDirectExchange": SortMethods.SortDirectExchange,
            "QuickSort": SortMethods.QuickSort,
            "ShellSort": SortMethods.ShellSort,
        }

    def generate_random_array(self, size: int) -> list[int]:
        if size <= 0:
            raise ValueError("Размер должен быть больше 0.")

        rand_gen = random.SystemRandom()
        return [rand_gen.randint(1, 10) for _ in range(size)]

    def sort_array(self, arr: list[int], sorted_percent: int) -> list[int]:
        if not (0 <= sorted_percent <= 100):
            raise ValueError("Процент должен быть от 0 до 100.")
        end = round(len(arr) * (sorted_percent / 100))
        sorted_part = sorted(arr[:end])
        return sorted_part + arr[end:]

    def calculation_time(
        self,
        sort_func: Callable[[list[int]], None],
        array: list[int],
    ) -> float:
        start_time = time.time()
        sort_func(array)
        end_time = time.time()
        return end_time - start_time

    def get_timings(self, size: int = 5000, sort_percent: int = 50) -> TimingsSort:
        if size <= 0:
            raise ValueError("Размер должен быть больше 0.")
        if not (0 <= sort_percent <= 100):
            raise ValueError("Процент должен быть от 0 до 100.")

        results = []
        array = self.generate_random_array(size)
        array = self.sort_array(array, sort_percent)

        for name, sort_func in self.sort_methods.items():
            sort_time = self.calculation_time(sort_func, array.copy())
            results.append(TimingSort(name=name, massive=size, time=sort_time))

        return TimingsSort(data=results)
