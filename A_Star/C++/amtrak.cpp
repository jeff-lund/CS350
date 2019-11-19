#include <iostream>
#include <string>
#include <cstring>
#include <unordered_map>
#include <vector>
#include <unordered_set>
#include <fstream>

#define NEIGHBOR g->edges[i].dest

using namespace std;

const float INFTY = 99999.0;

struct Edge {
  Edge();
  Edge(char*, char*, float);
  string src;
  string dest;
  float weight;
};

struct Graph {
  Graph();
  int nvertices;
  vector<Edge> edges;
  unordered_set<string> cities;
  unordered_map<string, unordered_map<string, float>> heuristic;
};

Graph::Graph() {
  nvertices = 0;
}

Edge::Edge() {}
Edge::Edge(char* s, char* d, float w) {
  src = s;
  dest = d;
  weight = w;
}

void set_heuristic(Graph *g) {
    char src[100], dst[100];
    float wt;
    ifstream f;
    f.open("euclidian.txt");
    
    f.get(src, 100, ' ');
    f.ignore(100, ' ');
    while(!f.eof()) {
        f.get(dst, 100, ' ');
        f >> wt;
        f.ignore(100, '\n');
        g->heuristic[src][dst] = wt;
        f.get(src, 100, ' ');
        f.ignore(100, ' ');
    }
    f.close();
}

Graph* process_file(void) {
  string fname = "routes.txt";
  Graph * g = new Graph;
  ifstream f;
  char bufsrc[100], bufdst[100];
  float weight;
  f.open(fname);
  while(!f.eof()) {
    f.ignore(100, '(');
    f.get(bufsrc, 100, ',');
    if(f.eof())
      break;
    f.ignore(100, ' ');
    f.get(bufdst, 100, ',');
    f.ignore();
    f >> weight;
    f.ignore(100, '\n');
    g->edges.push_back(Edge(bufsrc, bufdst, weight));
    g->edges.push_back(Edge(bufdst, bufsrc, weight));
    g->cities.insert(bufsrc);
    g->cities.insert(bufdst);
  }
  f.close();
  g->nvertices = g->cities.size();
  set_heuristic(g);
  return g;
}

string get_min(unordered_set<string> *openSet, unordered_map<string, float> *scores) {
  float min = INFTY;
  string current_low;

  for(auto& city: *openSet) {
    if((*scores)[city] < min) {
      min = (*scores)[city];
      current_low = city;
    }
  }
  openSet->erase(current_low);
  return current_low;
}

void make_path(unordered_map<string, string> cameFrom, string current)
{
  vector<string> path;
  path.push_back(current);
  while(cameFrom.find(current) != cameFrom.end()) {
    current = cameFrom[current];
    path.push_back(current);
  }
  for(int i = path.size() - 1; i >= 1; --i) {
    cout << path[i] << " --> ";
  }
  cout << path[0] << endl;
}

float a_star(Graph *g, string start, string end) {
  int n = g->edges.size();
  unordered_map<string, string> cameFrom;
  unordered_map<string, float> gscore, fscore;
  unordered_set<string> openSet;
  string current;
  float tenative;
  // city doesnt exist, just end
  if(!g->cities.count(start) || !g->cities.count(end))
    return -1.0;
  // Set up scoring maps
  for(const auto& elem:g->cities) {
    gscore[elem] = INFTY;
    fscore[elem] = INFTY;
  }
  gscore[start] = 0;
  fscore[start] = 0;

  openSet.insert(start);

  while(!openSet.empty()) {
    current = get_min(&openSet, &fscore);
    if(current == end) {
      make_path(cameFrom, current);
      return gscore[end];
    }
    // adjust neighbors score
    for(int i = 0; i < n; ++i) {
      if(g->edges[i].src != current)
        continue;
      tenative = gscore[current] + g->edges[i].weight;
      if(tenative < gscore[NEIGHBOR]) {
        cameFrom[NEIGHBOR] = current;
        gscore[NEIGHBOR] = tenative;
        fscore[NEIGHBOR] = gscore[NEIGHBOR]
            + g->heuristic[current][NEIGHBOR];
        openSet.insert(NEIGHBOR);
      }
    }
  }

  return 0.0;
}


int main(int argc, char** argv)
{
  if(argc < 3) {
    cout << "Usage: ./amtrak <start> <end>" << endl;
    return 0;
  }
  string start(argv[1]);
  string goal(argv[2]);
  Graph *g = process_file();
  float distance = a_star(g, start, goal);
  cout << "Total distance traveled: " << distance << "." << endl;

  delete g;
  return 0;
}
