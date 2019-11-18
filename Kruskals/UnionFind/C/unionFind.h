struct Node {
    char *label;
    struct Node* parent;
    struct Node *next;
};

struct UnionFind {
    struct Node *root;
};

void initUnionFind(struct UnionFind*);
void makeset(struct UnionFind*, const char*);
int find(struct UnionFind*, const char*, char*);
int merge(struct UnionFind*, const char*, const char*);
