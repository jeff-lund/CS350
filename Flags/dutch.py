# Dutch flag
# Usage python3 dutch.py <nred> <nwhite> <nblue>

from random import shuffle
from sys import argv

RED = '\033[1;31m'
WHITE = '\033[1;37m'
BLUE = '\033[1;34m'
RESET = '\033[0m'

def pprint(arr):
    for item in arr:
        if item == 'r':
            color = RED
        elif item == 'b':
            color = BLUE
        else:
            color = WHITE
        print(color, item, end='')
    print(RESET)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def double_partition(colors):
    '''
    Method for partitioning Dutch flag colors in 2 passes
    '''
    length = len(colors)
    # Partition Red from the rest of the list
    red_end = 0
    for i in range(length):
        if colors[i] == 'r':
            swap(colors, i, red_end)
            red_end += 1
    # Use similar approach to Hoare's Partitioning Algorithm
    # to partition blue and whites on the subarray that starts
    # after the reds
    # Scan from both the left and right swapping when a pair of elements
    # is found out of place
    # Stop scanning when the left and right indices meet or cross
    i = red_end
    if colors[i] == 'r':
        i += 1
    j = length - 1

    while i < j:
        while i < length and colors[i] == 'w':
            i += 1
        while j > red_end and colors[j] == 'b':
            j -= 1
        swap(colors, i, j)
    # Need to undo last swap
    swap(colors, i, j)


def better_dutch(colors):
    ''' 
    More efficient implementation of partitioning the Dutch flag
    Array is subdivided 4 secions
    Lo, Mid, High, and Unknown
    Anything before Lo is red
    Anthing from [Lo, Mid) is white
    and after High is blue
    Between the Mid and High sections is unknown
    The goal is to shrink the unknown section while maintaining
    these conditions.
    '''
    lo = 0 
    mid = 0
    high = len(colors) - 1
    # When Mid and High cross all elements are in the correct partition
    while mid <= high:
        if colors[mid] == 'r':
            swap(colors, lo, mid)
            lo += 1
            mid += 1
        elif colors[mid] == 'b':
            swap(colors, mid, high)
            high -= 1
        else:
            mid += 1

r, w, b = map(int, argv[1:4])
colors = ['r'] * r + \
        ['w'] * w + \
        ['b'] * b 

shuffle(colors)
pprint(colors)
print('-' * 80)
input("Ready to partition")
double_partition(colors)
#better_dutch(colors)
pprint(colors)
