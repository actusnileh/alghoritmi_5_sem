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
        root = self.root
        if self.search(k):
            return
        if len(root.keys) == (2 * self.t) - 1:  # Корень переполнен
            new_root = BTreeNode()
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, k)

    def _split_child(self, parent, i):
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
        if node is None:
            node = self.root

        for i in range(len(node.keys)):
            if not node.leaf:
                self.traverse(node.children[i])
            print(node.keys[i], end=" ")

        if not node.leaf:
            self.traverse(node.children[len(node.keys)])

    def traverse_as_dict(self, node=None):
        if node is None:
            node = self.root

        tree_node = {
            "name": ", ".join(map(str, node.keys)),
            "children": [],
        }

        if not node.leaf:
            for child in node.children:
                tree_node["children"].append(
                    self.traverse_as_dict(child),
                )

        return tree_node

    def delete(self, k, node=None):
        """Удаление ключа k из B-дерева"""
        if node is None:
            node = self.root

        t = self.t
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        # Случай 1: Ключ находится в узле
        if i < len(node.keys) and node.keys[i] == k:
            if node.leaf:
                node.keys.pop(i)
            else:
                self._delete_internal_node(node, k, i)
        else:
            if node.leaf:
                return  # Ключ не найден
            flag = i == len(node.keys)  # Последний ребенок?
            if len(node.children[i].keys) < t:
                self._fill(node, i)
            if flag and i > len(node.keys):
                self.delete(k, node.children[i - 1])
            else:
                self.delete(k, node.children[i])

    def _delete_internal_node(self, node, k, i):
        """Удаление ключа из внутреннего узла"""
        t = self.t
        if len(node.children[i].keys) >= t:
            pred = self._get_predecessor(node, i)
            node.keys[i] = pred
            self.delete(pred, node.children[i])
        elif len(node.children[i + 1].keys) >= t:
            succ = self._get_successor(node, i)
            node.keys[i] = succ
            self.delete(succ, node.children[i + 1])
        else:
            self._merge(node, i)
            self.delete(k, node.children[i])

    def _get_predecessor(self, node, i):
        """Возвращает предшественника ключа"""
        current = node.children[i]
        while not current.leaf:
            current = current.children[-1]
        return current.keys[-1]

    def _get_successor(self, node, i):
        """Возвращает преемника ключа"""
        current = node.children[i + 1]
        while not current.leaf:
            current = current.children[0]
        return current.keys[0]

    def _fill(self, node, i):
        """Пополнение узла при недостатке ключей"""
        t = self.t
        if i != 0 and len(node.children[i - 1].keys) >= t:
            self._borrow_from_prev(node, i)
        elif i != len(node.keys) and len(node.children[i + 1].keys) >= t:
            self._borrow_from_next(node, i)
        else:
            if i != len(node.keys):
                self._merge(node, i)
            else:
                self._merge(node, i - 1)

    def _borrow_from_prev(self, node, i):
        """Заимствование ключа у предыдущего узла"""
        child = node.children[i]
        sibling = node.children[i - 1]

        child.keys.insert(0, node.keys[i - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

        node.keys[i - 1] = sibling.keys.pop()

    def _borrow_from_next(self, node, i):
        """Заимствование ключа у следующего узла"""
        child = node.children[i]
        sibling = node.children[i + 1]

        child.keys.append(node.keys[i])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))

        node.keys[i] = sibling.keys.pop(0)

    def _merge(self, node, i):
        """Слияние двух узлов"""
        child = node.children[i]
        sibling = node.children[i + 1]

        child.keys.append(node.keys.pop(i))
        child.keys.extend(sibling.keys)

        if not child.leaf:
            child.children.extend(sibling.children)

        node.children.pop(i + 1)
