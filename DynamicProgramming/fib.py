from sys import argv

count = 0

def fib(n):
    global count
    count += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage: python3 fib.py <INT>")
    else:
        n = int(argv[1])
        print("The {}th fibonnaci number is {}".format(n, fib(n)))
        print("Total calls made:", count)
