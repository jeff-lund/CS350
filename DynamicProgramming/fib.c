#include <stdio.h>
#include <stdlib.h>

long fib( long n)
{
    if(n <= 1)
        return n;
    return fib(n - 1) + fib(n -2);
}

int main(int argc, char **argv) {
    long n = atoi(argv[1]);
    printf("%ld\n", fib(n));

    return 0;
}
