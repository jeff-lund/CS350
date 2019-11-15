class TreeNode:
    def __init__(self, val):
        self.val = val
        self.parent = None

    def attach(self, parent):
        self.parent = parent

    def __repr__(self):
        if self.parent == None:
            p = "None"
        else:
            p = str(self.parent.val)
        return "{} -> {}".format(str(self.val), p)

class UnionFind:
    def __init__(self):
        self.refs = {}
        self.trees = []
    
    def makeset(self, x):
        # Keys must be unique
        if x in self.refs:
            raise KeyError
        self.refs[x] = len(self.trees) 
        self.trees.append(TreeNode(x))

    def find(self, x):
        current = self.trees[self.refs[x]]
        while current.parent != None:
            current = current.parent
        return current.val
    
    def union(self, x, y):
        parent_x = self.trees[self.refs[self.find(x)]]
        parent_y = self.trees[self.refs[self.find(y)]]
        parent_x.attach(parent_y)

    def __repr__(self):
        return ', '.join(map(str, self.trees))


if __name__ == '__main__':
    u = UnionFind()
    u.makeset('apple')
    u.makeset('tree')
    u.makeset('hatchet')
    print(u)
    u.union('apple', 'tree')
    print(u)
    u.union('tree', 'hatchet')
    print(u)
    print(u.find('tree'))
    print(u.find('apple'))
