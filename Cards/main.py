from enum import Enum
from cards import Suit, Rank, Card
import random
import sys

def create_deck():
    deck = []
    for r in Rank:
        for s in Suit:
            deck.append(Card(suit=s, rank=r))
    return deck

def selection_sort(arr, key):
    n = len(arr)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if key(arr[j]) < key(arr[m]):
                m = j
        arr[i], arr[m] = arr[m], arr[i]

def insertion_sort(arr, key):
    n = len(arr)
    for i in range(1, n):
        v = arr[i]
        j = i - 1
        while j >= 0 and key(arr[j]) > key(v):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v

def merge(b, c, a, key):
    i = j = k = 0
    p = len(b)
    q = len(c)
    while i < p and j < q:
        if key(b[i]) <= key(c[j]):
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1
    if i == p:
        for ele in c[j:]:
            a[k] = ele
            k += 1
    else:
        for ele in b[i:]:
            a[k] = ele
            k += 1

def mergesort(arr, key):
    n = len(arr)
    if n > 1:
        b = arr[:n // 2].copy()
        c = arr[n // 2:].copy()
        mergesort(b, key)
        mergesort(c, key)
        merge(b, c, arr, key)

def timsort(arr, key):
    arr.sort(key=key)

def pprint(deck, msg):
    print(msg)
    print("-" * 50)
    for card in deck:
        print(card)
    print("-" * 50)

if __name__=='__main__':
    func = None
    if len(sys.argv) == 1:
        func = timsort
    elif sys.argv[1] == 'insert':
        func = insertion_sort
    elif sys.argv[1] == 'select':
        func = selection_sort
    elif sys.argv[1] == 'merge':
        func = mergesort
    else:
        print("Invalid option.")
        print("Usage: python3 main.py <insert | select | merge>")
        sys.exit()

    deck = create_deck()
    random.shuffle(deck)
    pprint(deck, "Shuffled deck")
   
    func(deck, key=lambda x: x.rank)
    pprint(deck, "Sorted by rank")
    
    func(deck, key=lambda x: x.suit)
    pprint(deck, "Sorted by suit")
