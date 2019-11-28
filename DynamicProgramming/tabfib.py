from sys import argv

count = 0
memo = {}

def fib(n):
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs[n]

if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage: python3 fib.py <INT>")
    else:
        n = int(argv[1])
        print("The {}th fibonnaci number is {}".format(n, fib(n)))
