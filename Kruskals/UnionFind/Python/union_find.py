class UnionFind:
    def __init__(self):
        self.trees = {}
    
    def makeset(self, x):
        # Keys must be unique
        if x in self.trees:
            raise KeyError
        self.trees[x] = None

    def find(self, x):
        while self.trees[x] != None:
            x = self.trees[x]
        return x
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        self.trees[parent_x] = parent_y

    # magic methods - operator overloading
    # overloads printing of UnionFind objects
    def __repr__(self):
        ret = ""
        for k, v in self.trees.items():
            ret += str(k) + ' -> ' + str(v) + ', '
        return ret

    # overloads len function, returns number of elements 
    def __len__(self):
        return len(self.trees)

    # overloads 'in' keyword usage. 'Portland' in UF will now work
    def __contains__(self, item):
        return item in self.trees

if __name__ == '__main__':
    u = UnionFind()
    u.makeset('apple')
    u.makeset('tree')
    u.makeset('hatchet')
    print('bool check:', 'tree' in u)
    print(u)
    u.union('apple', 'tree')
    print(u)
    u.union('tree', 'hatchet')
    print(u)
    print(u.find('tree'))
    print(u.find('apple'))
