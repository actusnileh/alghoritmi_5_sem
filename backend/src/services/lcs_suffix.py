class STree:
    def __init__(self, input=""):
        self.root = _SNode()
        self.root.depth = 0
        self.root.idx = 0
        self.root.parent = self.root
        self.root._add_suffix_link(self.root)

        if not input == "":
            self.build(input)

    def _check_input(self, input):
        if isinstance(input, str):
            return "st"
        elif isinstance(input, list):
            if all(isinstance(item, str) for item in input):
                return "gst"

        raise ValueError(
            "String argument should be of type String or a list of strings",
        )

    def build(self, x):
        type_symbol = self._check_input(x)

        if type_symbol == "st":
            x += next(self._terminalSymbolsGenerator())
            self._build(x)
        if type_symbol == "gst":
            self._build_generalized(x)

    def _build(self, x):
        self.word = x
        self._build_McCreight(x)

    def _build_McCreight(self, x):
        u = self.root
        d = 0
        for i in range(len(x)):
            while u.depth == d and u._has_transition(x[d + i]):
                u = u._get_transition_link(x[d + i])
                d = d + 1
                while d < u.depth and x[u.idx + d] == x[i + d]:
                    d = d + 1
            if d < u.depth:
                u = self._create_node(x, u, d)
            self._create_leaf(x, i, u, d)
            if not u._get_suffix_link():
                self._compute_slink(x, u)
            u = u._get_suffix_link()
            d = d - 1
            if d < 0:
                d = 0

    def _create_node(self, x, u, d):
        i = u.idx
        p = u.parent
        v = _SNode(idx=i, depth=d)
        v._add_transition_link(u, x[i + d])
        u.parent = v
        p._add_transition_link(v, x[i + p.depth])
        v.parent = p
        return v

    def _create_leaf(self, x, i, u, d):
        w = _SNode()
        w.idx = i
        w.depth = len(x) - i
        u._add_transition_link(w, x[i + d])
        w.parent = u
        return w

    def _compute_slink(self, x, u):
        d = u.depth
        v = u.parent._get_suffix_link()
        while v.depth < d - 1:
            v = v._get_transition_link(x[u.idx + v.depth + 1])
        if v.depth > d - 1:
            v = self._create_node(x, v, d - 1)
        u._add_suffix_link(v)

    def _build_generalized(self, xs):
        terminal_gen = self._terminalSymbolsGenerator()

        _xs = "".join([x + next(terminal_gen) for x in xs])
        self.word = _xs
        self._generalized_word_starts(xs)
        self._build(_xs)
        self.root._traverse(self._label_generalized)

    def _label_generalized(self, node):
        if node.is_leaf():
            x = {self._get_word_start_index(node.idx)}
        else:
            x = {
                n for ns in node.transition_links.values() for n in ns.generalized_idxs
            }
        node.generalized_idxs = x

    def _get_word_start_index(self, idx):
        i = 0
        for _idx in self.word_starts[1:]:
            if idx < _idx:
                return i
            else:
                i += 1
        return i

    def lcs(self, stringIdxs=-1):
        if stringIdxs == -1 or not isinstance(stringIdxs, list):
            stringIdxs = set(range(len(self.word_starts)))
        else:
            stringIdxs = set(stringIdxs)

        deepestNode = self._find_lcs(self.root, stringIdxs)
        start = deepestNode.idx
        end = deepestNode.idx + deepestNode.depth
        return self.word[start:end]

    def _find_lcs(self, node, stringIdxs):
        nodes = [
            self._find_lcs(n, stringIdxs)
            for n in node.transition_links.values()
            if n.generalized_idxs.issuperset(stringIdxs)
        ]

        if nodes == []:
            return node

        deepestNode = max(nodes, key=lambda n: n.depth)
        return deepestNode

    def _generalized_word_starts(self, xs):
        self.word_starts = []
        i = 0
        for n in range(len(xs)):
            self.word_starts.append(i)
            i += len(xs[n]) + 1

    def _terminalSymbolsGenerator(self):
        UPPAs = list(
            list(range(0xE000, 0xF8FF + 1))
            + list(range(0xF0000, 0xFFFFD + 1))
            + list(range(0x100000, 0x10FFFD + 1)),
        )
        for i in UPPAs:
            yield (chr(i))

        raise ValueError("To many input strings.")

    def get_tree_structure(self):
        return self._get_node_structure(self.root)

    def _get_node_structure(self, node):
        node_structure = {"idx": node.idx, "depth": node.depth, "transitions": {}}

        for suffix, child in node.transition_links.items():
            node_structure["transitions"][suffix] = self._get_node_structure(child)

        return node_structure


class _SNode:
    __slots__ = [
        "_suffix_link",
        "transition_links",
        "idx",
        "depth",
        "parent",
        "generalized_idxs",
    ]

    def __init__(self, idx=-1, parentNode=None, depth=-1):
        # Links
        self._suffix_link = None
        self.transition_links = {}
        # Properties
        self.idx = idx
        self.depth = depth
        self.parent = parentNode
        self.generalized_idxs = {}

    def __str__(self):
        return (
            "SNode: idx:"
            + str(self.idx)
            + " depth:"
            + str(self.depth)
            + " transitons:"
            + str(list(self.transition_links.keys()))
        )

    def _add_suffix_link(self, snode):
        self._suffix_link = snode

    def _get_suffix_link(self):
        if self._suffix_link is not None:
            return self._suffix_link
        else:
            return False

    def _get_transition_link(self, suffix):
        return (
            False
            if suffix not in self.transition_links
            else self.transition_links[suffix]
        )

    def _add_transition_link(self, snode, suffix):
        self.transition_links[suffix] = snode

    def _has_transition(self, suffix):
        return suffix in self.transition_links

    def is_leaf(self):
        return len(self.transition_links) == 0

    def _traverse(self, f):
        for node in self.transition_links.values():
            node._traverse(f)
        f(self)
