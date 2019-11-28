from sys import argv

def fib(n):
    x = 0
    y = 1
    for i in range(2, n + 1):
        temp = x + y
        x = y
        y = temp
    return temp

if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage: python3 goodfib.py <INT>")
    else:
        n = int(argv[1])
        print("The {}th fibonnaci number is {}".format(n, fib(n)))
