class BNode:
    def __init__(self, leaf: bool = False):
        self.leaf = leaf  # Флаг, указывающий, является ли этот узел листом (true) или внутренним узлом (false)
        self.keys = []  # Список ключей, хранимых в узле
        self.children = []  # Список дочерних узлов (только для внутренних узлов)


class BTree:
    def __init__(self, t: int):
        self.root = BNode(
            True,
        )  # Инициализируем дерево с корневым узлом, который изначально является листом
        self.t = t  # Минимальная степень дерева. Это параметр, который определяет
        # минимальное и максимальное количество ключей в узле

    def print_tree(self, x, level=0):
        """Рекурсивно выводит дерево на экран, начиная с узла 'x'."""
        if not x.keys:  # Если у узла нет ключей, его пропускаем
            return

        indent = "  " * level  # Отступ для отображения уровня узла
        print(f"{indent}Уровень {level}: {x.keys}")  # Выводим ключи узла и его уровень

        for (
            child
        ) in x.children:  # Рекурсивно вызываем эту функцию для всех дочерних узлов
            self.print_tree(child, level + 1)

    def split(self, parent, index):
        """Разделяет переполненный узел на два и перемещает средний ключ в родительский узел."""
        t = self.t  # Получаем минимальную степень
        full_node = parent.children[index]  # Получаем переполненный дочерний узел
        new_node = BNode(
            leaf=full_node.leaf,
        )  # Создаем новый узел (будет правой половиной)

        # Переносим ключи и детей из переполненного узла в новый
        new_node.keys = full_node.keys[t:]  # Переносим правую часть ключей в новый узел
        full_node.keys = full_node.keys[
            : t - 1
        ]  # Левую часть оставляем в оригинальном узле

        if (
            not full_node.leaf
        ):  # Если это внутренний узел, также переносим его дочерние узлы
            new_node.children = full_node.children[
                t:
            ]  # Правые дочерние узлы идут к новому узлу
            full_node.children = full_node.children[
                :t
            ]  # Левые остаются у оригинального

        # Вставляем новый узел в родительский узел
        parent.children.insert(
            index + 1,
            new_node,
        )  # Новый узел добавляем справа от переполненного
        parent.keys.insert(
            index,
            full_node.keys.pop(),
        )  # Средний ключ из переполненного узла переносим в родителя

    def insert_non_full(self, node, key):
        """Вставка ключа в узел, который не переполнен."""
        i = len(node.keys) - 1  # Индекс последнего ключа в узле

        if node.leaf:  # Если узел является листом
            node.keys.append(None)  # Добавляем заглушку в конец, чтобы сдвигать ключи
            while (
                i >= 0 and key < node.keys[i]
            ):  # Ищем правильную позицию для вставки ключа
                node.keys[i + 1] = node.keys[i]  # Сдвигаем ключи вправо
                i -= 1
            node.keys[i + 1] = key  # Вставляем ключ на найденное место
        else:
            # Ищем подходящий дочерний узел для спуска
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            # Если дочерний узел переполнен, разделяем его
            if len(node.children[i].keys) == 2 * self.t - 1:
                self.split(node, i)
                if (
                    key > node.keys[i]
                ):  # После разделения возможно, что нужно будет переместиться на следующий узел
                    i += 1
            self.insert_non_full(
                node.children[i],
                key,
            )  # Рекурсивно вставляем ключ в подходящий дочерний узел

    def insert_key(self, key):
        """Вставка ключа в дерево."""
        root = self.root
        if len(root.keys) == 2 * self.t - 1:  # Если корневой узел переполнен
            new_root = BNode(leaf=False)  # Создаем новый корневой узел
            new_root.children.append(root)  # Старый корневой узел становится дочерним
            self.root = new_root  # Новый узел становится корнем
            self.split(new_root, 0)  # Разделяем старый корень
            self.insert_non_full(new_root, key)  # Вставляем новый ключ в неполный узел
        else:
            self.insert_non_full(
                root,
                key,
            )  # Если корень не переполнен, просто вставляем ключ

    def search_key(self, key, node=None):
        """Поиск ключа в дереве."""
        node = node or self.root  # Начинаем поиск с корня, если узел не указан
        i = 0
        while (
            i < len(node.keys) and key > node.keys[i]
        ):  # Ищем место, где ключ может находиться
            i += 1

        if i < len(node.keys) and key == node.keys[i]:  # Если ключ найден
            return (node, i)  # Возвращаем узел и индекс ключа

        if node.leaf:  # Если это лист, а ключ не найден, то ключа в дереве нет
            return None

        return self.search_key(
            key,
            node.children[i],
        )  # Рекурсивно ищем ключ в подходящем дочернем узле
