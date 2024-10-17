class BNode:
    def __init__(self, leaf: bool = False):
        self.leaf = leaf  # Является ли узлом
        self.keys = []  # Список ключей
        self.children = []  # Список дочерних узлов


class BTree:
    def __init__(self, t):
        self.root = BNode(True)
        self.t = t

    def print_tree(self, x, level=0):
        print("Уровень", level, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        level += 1
        if len(x.children) > 0:
            for i in x.children:
                self.print_tree(i, level)

    def split(self, x, i):
        t = self.t
        y = x.children[i]
        z = BNode(y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t : (2 * t) - 1]
        y.keys = y.keys[0 : t - 1]
        if not y.leaf:
            z.child = y.children[t : 2 * t]
            y.child = y.children[0 : t - 1]

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.split(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.children[i], k)

    def insert_key(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BNode(False)  # Новый корень
            new_root.children.append(root)
            self.root = new_root
            self.split(new_root, 0)
            self.insert_non_full(new_root, k)
        else:
            self.insert_non_full(root, k)

    def search_key(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search_key(k, x.children[i])
        else:
            return self.search_key(k, self.root)
