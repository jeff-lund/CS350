#include <stdio.h>
#include <string.h>
#include "unionFind.h"

int main(int argc, char **argv) {
    char *strs[] = {"Apple", "Pear", "Blueberry", "Watermelon", "Peach"};
    char buffer[500];
    int n = 5;
    struct UnionFind u;
    
    initUnionFind(&u);
    
    for(int i = 0; i < n; ++i) 
        makeset(&u, strs[i]);

    if(!merge(&u, "Apple", "Pear"))
        printf("Merge 1 failed\n");
    if(!merge(&u, "Apple", "Blueberry"))
        printf("Merge 2 failed\n");
    if(!merge(&u, "Peach", "Watermelon"))
        printf("Merge 3 failed\n");

    find(&u, "Apple", buffer);
    printf("Parent of Apple is %s\n", buffer);
    find(&u, "Pear", buffer);
    printf("Parent of Pear is %s\n", buffer);
    find(&u, "Blueberry", buffer);
    printf("Parent of Blueberry is %s\n", buffer);
    find(&u, "Watermelon", buffer);
    printf("Parent of Watermelon is %s\n", buffer);
    find(&u, "Peach", buffer);
    printf("Parent of Peach is %s\n", buffer);
    
    return 0;
}
