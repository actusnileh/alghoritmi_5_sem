import io

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.value_per_weight = value / weight


def continuous_backpack(items, capacity):
    items = sorted(items, key=lambda x: x.value_per_weight, reverse=True)

    total_value = 0
    weight_used = 0
    fractions = []

    for item in items:
        if capacity == 0:
            break

        if item.weight <= capacity:
            total_value += item.value
            weight_used += item.weight
            fractions.append(1)
            capacity -= item.weight
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            weight_used += capacity
            fractions.append(fraction)
            capacity = 0

    return total_value, weight_used, fractions


def discrete_backpack(items, capacity):
    n = len(items)
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if items[i - 1].weight <= w:
                dp_table[i][w] = max(
                    dp_table[i - 1][w],
                    dp_table[i - 1][w - items[i - 1].weight] + items[i - 1].value,
                )
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    df_dp = pd.DataFrame(dp_table)
    return df_dp, dp_table[n][capacity]


def visualize_discrete_backpack(df_dp):
    step = 10
    df_filtered = df_dp.loc[
        :,
        df_dp.columns % step == 0,
    ]
    df_filtered.index = range(
        0,
        len(df_filtered),
    )

    plt.figure(figsize=(10, 8))
    sns.heatmap(df_filtered, annot=True, cmap="YlGnBu", fmt="g")
    plt.title("Таблица")
    plt.xlabel("Вес")
    plt.ylabel("Предмет")
    plt.xticks(rotation=45)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return buf


def visualize_continuous_backpack(items, capacity, total_value, weight_used, fractions):
    plt.figure(figsize=(10, 6))

    used_weights = []
    current_weight = 0

    for i, fraction in enumerate(fractions):
        if fraction == 1:
            current_weight += items[i].weight
        else:
            current_weight += items[i].weight * fraction

        used_weights.append(current_weight)

    item_labels = [f"Предмет {i + 1}" for i in range(len(items))]

    plt.bar(
        range(len(items)),
        used_weights,
        color="blue",
        alpha=0.7,
        label="Использованный вес",
    )

    plt.xticks(range(len(items)), item_labels)

    plt.axhline(y=capacity, color="r", linestyle="--", label="Емкость рюкзака")
    plt.title(
        f"Непрерывный рюкзак\nМаксимальная стоимость: {total_value}\nИспользованный вес: {weight_used}",
    )
    plt.xlabel("Предметы")
    plt.ylabel("Использованный вес")
    plt.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return buf
