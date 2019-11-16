#include <string>
#include <iostream>
#include "union_find.h"

using namespace std;

UnionFind::UnionFind() {
  ntrees = 0;
}

UnionFind::~UnionFind() {
  for(int i = 0; i < ntrees; ++i) {
    delete trees[i];
  }
}

void UnionFind::makeset(string s) {
  refs[s] = ntrees++;
  Node *n = new Node;
  n->parent = NULL;
  n->label = s;
  trees.push_back(n);
}

string UnionFind::find(string s) {
  int idx = refs[s];
  Node *current = trees[idx];
  while(current->parent) {
    current = current->parent;
  }
  return current->label;
}

void UnionFind::merge(string v, string u) {
  Node* parentV = trees[refs[v]];
  Node* parentU = trees[refs[u]];
  while(parentV->parent) {
    parentV = parentV->parent;
  }
  while(parentU->parent) {
    parentU = parentU->parent;
  }
  parentV->parent = parentU;
}
