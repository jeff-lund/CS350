#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 20

void quicksort(int*, int, int);
int partition(int*, int, int);
void swap(int*, int, int);
void pprint(int*, int);

int main(int argc, char **argv)
{
    srand(time(0));
    int arr[SIZE];
    for(int i = 0; i < SIZE; ++i) {
        arr[i] = rand() % 1000;
    }
    pprint(arr, SIZE);
    quicksort(arr, 0, SIZE - 1);
    pprint(arr, SIZE);
    return 0;
}


void quicksort(int arr[], int left, int right)
{
    int s;
    if(left < right) {
        s = partition(arr, left, right);
        quicksort(arr, left, s - 1);
        quicksort(arr, s + 1, right);
    }
}

int partition(int arr[], int left, int right)
{
    int pivot = arr[left];
    int i = left;
    int j = right + 1;
    do
    {
        do { ++i; } while(arr[i] < pivot);
        do { --j; } while(arr[j] > pivot);
        swap(arr, i, j);
    } while(i < j);
    swap(arr, i, j);
    swap(arr, left, j);
    return j;
}

void swap(int arr[], int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

void pprint(int arr[], int n)
{
    for(int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    printf("\n");
}
