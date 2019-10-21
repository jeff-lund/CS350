from sys import argv
from random import randint
from time import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        v = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v


if __name__ == '__main__':
    if len(argv) > 1:
        sz = int(argv[1])
        arr = [randint(1, 1000) for _ in range(sz)]
        #print(arr)
        start = time()
        insertion_sort(arr)
        end = time()
        #print(arr)
        print(end - start)
    else:
        # performs automated testing
        x = []
        y = []
        sizes = [10, 50, 100, 200, 500, 1000, 1200, 1500, 2000, 2500, 3000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000]
        for sz in sizes:
            t = 0
            print("running size", sz)
            for _ in range(10):
                arr = [randint(1, 10000) for _ in range(sz)]
                start = time()
                insertion_sort(arr)
                end = time()
                t += (end - start) * 1000
            x.append(sz)
            y.append(t // 10)
    
        # Plot results of tests
        plt.plot(x, y)
        plt.xlabel("n (size of array)")
        plt.ylabel("time (ms)")
        plt.show()
        #plt.savefig("python_running_times.png", format='png')
