from sys import argv
import random
import math
import argparse

def tokuda(n):
    ''' Generate the nth value of the Tokuda Sequence '''
    return math.ceil( (9 * (9 / 4)**n - 4) / 5)

def generate_sequence(n):
    ''' 
    Generates the full Tokuda sequence with values less
    than the size of the array we are sorting
    '''
    m = 0
    sequence = []
    val = tokuda(m)
    # Continue to add increasing values until we exceed the 
    # size of the input array
    while val < n:
        sequence.append(val)
        m += 1
        val = tokuda(m)

    return sequence
        
def shellsort(arr):
    n = len(arr)
    gaps = generate_sequence(n)
    for gap in reversed(gaps):
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--printer', 
            help='print pre- and post-sorted array', 
            action='store_true')
    parser.add_argument('-s', '--size', 
            help='size of array to sort',
            type=int, default=10)
    args = parser.parse_args()
    # Set up parsed flags
    printing = args.printer
    size = args.size
    
    arr = [x for x in range(size)]
    random.shuffle(arr)
    
    if printing:
        print(arr)
    
    shellsort(arr)
    
    if printing:
        print(arr)
