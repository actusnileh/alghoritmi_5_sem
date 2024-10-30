# Традиционно, узлы АВЛ-дерева хранят не высоту, а разницу высот правого и левого поддеревьев
# (так называемый balance factor), которая может принимать только три значения -1, 0 и 1
class AVLNode:
    def __init__(self, key, left=None, right=None):
        self.key = key  # Ключ узла
        self.left = left  # Указатель на левое поддерево
        self.right = right  # Указатель на правое поддерево
        self.height = 1  # Высота поддерева с корнем в данном узле


def height(node: AVLNode):
    # Обёртка для поля height, может работать с пустыми деревьями
    return node.height if node else 0


def bfactor(node: AVLNode):
    # Вычисляем баланс фактор, не работает с пустыми деревьями
    return height(node.right) - height(node.left)


def fixheight(node: AVLNode):
    # Восстанавливаем корректное значение поля height заданного узла
    hl = height(node.left)
    hr = height(node.right)
    node.height = max(hl, hr) + 1


def rotate_right(node: AVLNode):
    # Правый поворот
    q: AVLNode = node.left
    node.left = q.right
    q.right = node
    fixheight(node)
    fixheight(q)
    return q


def rotate_left(node: AVLNode):
    # Левый поворот
    p: AVLNode = node.right
    node.right = p.left
    p.left = node
    fixheight(node)
    fixheight(p)
    return p


def balance(node: AVLNode):
    # Восстановление баланса узла
    fixheight(node)
    if bfactor(node) == 2:
        if bfactor(node.right) < 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)
    if bfactor(node) == -2:
        if bfactor(node.left) > 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)
    return node  # Балансировка не нужна


def insert(node: AVLNode, key):
    if not node:
        return AVLNode(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return balance(node)


def findmin(node: AVLNode):
    return findmin(node.left) if node.left else node


def removemin(node: AVLNode):
    if node.left is None:
        return node.right
    node.left = removemin(node.left)
    return balance(node)


def remove(node: AVLNode, key):
    if not node:
        return None

    if key < node.key:
        node.left = remove(node.left, key)
    elif key > node.key:
        node.right = remove(node.right, key)
    else:
        q = node.left
        r = node.right
        if r is None:
            return q

        min_node = findmin(r)
        min_node.right = removemin(r)
        min_node.left = q
        return balance(min_node)

    return balance(node)


def in_order_traversal(node: AVLNode):
    if node:
        in_order_traversal(node.left)
        print(node.key, end=" ")
        in_order_traversal(node.right)


def traverse_as_dict(node: AVLNode):
    if node is None:
        return None

    tree_node = {
        "name": node.key,  # Используем ключ узла
        "children": [],  # Инициализируем список детей
    }

    if node.left or node.right:
        if node.left:
            tree_node["children"].append(traverse_as_dict(node.left))
        if node.right:
            tree_node["children"].append(traverse_as_dict(node.right))

    return tree_node
