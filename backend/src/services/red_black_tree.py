class Node:
    def __init__(self, data, color="red"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color="black")
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.color = "red"

        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k != self.root and k.parent.color == "red":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "red":
                    k.parent.color = "black"
                    u.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "red":
                    k.parent.color = "black"
                    u.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
        self.root.color = "black"

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete(self, data):
        z = self.root
        while z != self.NIL and z.data != data:
            if data < z.data:
                z = z.left
            else:
                z = z.right

        if z == self.NIL:
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "black":
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "red":
                    s.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == "black" and s.right.color == "black":
                    s.color = "red"
                    x = x.parent
                else:
                    if s.right.color == "black":
                        s.left.color = "black"
                        s.color = "red"
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = "black"
                    s.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "red":
                    s.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == "black" and s.left.color == "black":
                    s.color = "red"
                    x = x.parent
                else:
                    if s.left.color == "black":
                        s.right.color = "black"
                        s.color = "red"
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = "black"
                    s.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"

    def traverse_as_dict(self, node):
        if node == self.NIL:
            return None

        tree_node = {
            "name": f"{node.data}",
            "color": f"{"Черный" if node.color == "black" else "Красный"}",
            "children": [],
        }

        if node.left != self.NIL or node.right != self.NIL:
            if node.left != self.NIL:
                tree_node["children"].append(self.traverse_as_dict(node.left))
            if node.right != self.NIL:
                tree_node["children"].append(self.traverse_as_dict(node.right))

        return tree_node
