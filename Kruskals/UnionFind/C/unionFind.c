#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "unionFind.h"

void initUnionFind(struct UnionFind *u) {
    u->root = NULL;
}

void makeset(struct UnionFind *u, const char* str) {
    // create new node
    struct Node *n = malloc(sizeof(struct Node));
    // set name of node
    n->label = malloc(sizeof(char) * (strlen(str) + 1));
    strcpy(n->label, str);
    // move to front of linked list
    n->parent = NULL;
    n->next = u->root;
    u->root = n;
}

// Parent of the item searched for will be returned in 
// the buffer argument. It is the responsibility of the user
// to ensure buffer is large enough to contain the returned label.
// Returns 1 on success, 0 if search does not appear in the list
int find(struct UnionFind* u, const char* search, char* buffer) {
    struct Node* current = u->root;
    // Find correct node
    while(current && strcmp(search, current->label) != 0) {
        current = current->next;
    }
    // Search not found in list
    if(!current)
        return 0;
    // Find parent of node searched for
    while(current->parent)
        current = current->parent;
    // Copy over name from parent into buffer
    strcpy(buffer, current->label);
    return 1;
}

// If one or both of the strings being searched for does not
// exist in the list then 0 is returned, otherwise returns 1
int merge(struct UnionFind* u, const char* x, const char* y) {
    struct Node *xNode, *yNode;
    xNode = u->root;
    // Find nodes to union
    while(xNode && strcmp(xNode->label, x) != 0) {
        xNode = xNode->next;
    }
    yNode = u->root;
    while(yNode && strcmp(yNode->label, y) != 0) {
        yNode = yNode->next;
    }
    // One of the nodes not found
    if(!xNode || !yNode)
        return 0;
    
    // Find parent of each node
    while(xNode->parent)
        xNode = xNode->parent;
    while(yNode->parent)
        yNode = yNode->parent;
    xNode->parent = yNode;
    
    return 1;
}
