#include <iostream>
#include "union_find.h"
#include <string>

int main(int argc, char **argv) {
  string strs[] = {"Portland", "Seattle", "Boston", "New York", "Bellingham"};
  int n = 5;
  UnionFind u;
  for(int i = 0; i < n; ++i) {
    u.makeset(strs[i]);
  }
  cout <<  u.find("Portland") << endl;
  u.merge("Portland", "Seattle");
  u.merge("Bellingham", "Boston");
  u.merge("New York", "Portland");
  for(int i = 0; i < n; ++i) {
    cout << "For city " << strs[i] << " the parent is " << u.find(strs[i]) << endl;
  }

  return 0;
}
