from sys import argv

count = 0
memo = {}

def fib(n):
    global count
    global memo
    count += 1
    if n not in memo:
        if n == 0:
            memo[0] = 0
        elif n == 1:
            memo[1] = 1
        else:
            memo[n] = fib(n - 1) + fib(n -2)
    
    return memo[n]


if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage: python3 fib.py <INT>")
    else:
        n = int(argv[1])
        print("The {}th fibonnaci number is {}".format(n, fib(n)))
        print("Total call:", count)
