#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

struct Node {
  string label;
  Node* parent;
};

class UnionFind {
  public:
    UnionFind();
    ~UnionFind();
    void makeset(string);
    string find(string);
    // Turns out union is a keyword in C++ :(
    void merge(string, string);

  private:
    unordered_map<string, int> refs;
    vector<Node*> trees;
    int ntrees;
};
