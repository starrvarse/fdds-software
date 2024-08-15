class BTreeNode:
    """
    Node class for B-tree.
    """

    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    """
    B-tree data structure for indexing.
    """

    def __init__(self, t):
        """
        Initialize a B-tree with minimum degree t.
        
        :param t: The minimum degree of the B-tree.
        """
        self.root = BTreeNode(True)
        self.t = t

    def search(self, k, x=None):
        """
        Search for a key in the B-tree.
        
        :param k: The key to search for.
        :param x: The node to start the search from (default is root).
        :return: The node containing the key, or None if not found.
        """
        if x is None:
            x = self.root
        
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        
        if i < len(x.keys) and k == x.keys[i]:
            return (x, i)
        
        if x.leaf:
            return None
        
        return self.search(k, x.children[i])

    def insert(self, k):
        """
        Insert a key into the B-tree.
        
        :param k: The key to insert.
        """
        r = self.root
        if len(r.keys) == (2 * self.t) - 1:
            s = BTreeNode(leaf=False)
            self.root = s
            s.children.insert(0, r)
            self._split_child(s, 0)
            self._insert_non_full(s, k)
        else:
            self._insert_non_full(r, k)

    def _insert_non_full(self, x, k):
        """
        Helper function to insert a key into a non-full node.
        
        :param x: The node to insert into.
        :param k: The key to insert.
        """
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_non_full(x.children[i], k)

    def _split_child(self, x, i):
        """
        Helper function to split a full child node.
        
        :param x: The parent node.
        :param i: The index of the child to split.
        """
        t = self.t
        y = x.children[i]
        z = BTreeNode(y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t - 1]
        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]
