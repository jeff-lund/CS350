#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void insertionSort(int arr[], int n)
{
	int v, j;
	for(int i = 1; i < n; ++i)
	{
		v = arr[i];
		j = i - 1;
		while(j >= 0 && arr[j] > v)
		{
			arr[j + 1] = arr[j];
			--j;
		}
		arr[j + 1] = v;
	}
}

int main(int argc, char **argv)
{
	int n;
	int *arr; 
	
	n = atoi(argv[1]);	
	arr = malloc(sizeof(int) * n);
	srand(time(0));

	for(int i = 0; i < n; ++i)
		arr[i] = rand() % 1000; 
	for(int i = 0; i < n; ++i)
		printf("%d ", arr[i]);
	printf("\n");
	insertionSort(arr, n);
	for(int i = 0; i < n; ++i)
		printf("%d ", arr[i]);
	printf("\n");

	return 0;
}
