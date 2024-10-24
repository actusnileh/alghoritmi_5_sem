class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf  # Является ли узел листом
        self.keys = []  # Ключи узла
        self.children = []  # Дочерние узлы


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)  # Изначально корень — это лист
        self.t = t  # Минимальная степень дерева

    def search(self, k, node=None):
        """Поиск ключа k в B-дереве"""
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        if i < len(node.keys) and k == node.keys[i]:
            return node, i  # Ключ найден

        if node.leaf:
            return None  # Ключ не найден в дереве

        return self.search(k, node.children[i])

    def insert(self, k):
        """Вставка нового ключа k в B-дерево"""
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:  # Корень переполнен
            new_root = BTreeNode()
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, k)

    def _split_child(self, parent, i):
        """Разделение переполненного дочернего узла"""
        t = self.t
        node_to_split = parent.children[i]
        new_node = BTreeNode(node_to_split.leaf)

        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, node_to_split.keys[t - 1])

        new_node.keys = node_to_split.keys[t : (2 * t - 1)]
        node_to_split.keys = node_to_split.keys[0 : t - 1]

        if not node_to_split.leaf:
            new_node.children = node_to_split.children[t : (2 * t)]
            node_to_split.children = node_to_split.children[0:t]

    def _insert_non_full(self, node, k):
        """Вставка ключа в неполный узел"""
        if node.leaf:
            i = len(node.keys) - 1
            node.keys.append(0)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            i = len(node.keys) - 1
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def traverse(self, node=None):
        """Обход дерева в порядке возрастания"""
        if node is None:
            node = self.root

        for i in range(len(node.keys)):
            if not node.leaf:
                self.traverse(node.children[i])
            print(node.keys[i], end=" ")

        if not node.leaf:
            self.traverse(node.children[len(node.keys)])

    def traverse_as_dict(self, node=None):
        """Возвращает дерево в виде словаря для визуализации"""
        if node is None:
            node = self.root

        # Формируем узел в формате, необходимом для визуализации
        tree_node = {
            "name": ", ".join(map(str, node.keys)),  # Объединяем ключи в строку
            "children": [],  # Инициализируем список детей
        }

        # Если узел не лист, рекурсивно обрабатываем дочерние узлы
        if not node.leaf:
            for child in node.children:
                tree_node["children"].append(
                    self.traverse_as_dict(child),
                )  # Добавляем дочерние узлы

        return tree_node
