import random
import re

"""Import list of words from english wordlist"""
def import_wordlist():
    return [w for w in open("english-words/words.txt",'r').readlines()]

"""Filter out any words that contain numbers"""
def filter_out_nums(word):
    for c in word:
        if c in '1234567890':
            return False
    return True

"""Filter out words beyond a certain length"""
def filter_beyond_len(n):
    return lambda w: len(w) <= n

print(list(filter(filter_out_nums, ['hello0','hello'])))

wl = import_wordlist()
print("Number of words including numbers", len(wl))
print("Excluding numbers", len(list(filter(filter_out_nums, wl))))

# Just deal with the "real" words for now and trim ws
wl = list(map(lambda s: s.strip(),filter(filter_out_nums, wl)))

# Filter out non alphanumeric characters
p = re.compile('^[a-zA-Z]*$')
wl = [w for w in wl if p.match(w)]

# Next, trim down to words less than a certain length
wl = list(filter(filter_beyond_len(5), wl))

# Make them all lowercase
chosen = [w.lower() for w in random.sample(wl, 3)]
print(chosen)

# Now we have our words for the wordsearch selected
# The next step is to lay them out in a grid
# This is the hard part
# We will set a target wordsearch puzzle dimension N
# and then attempt to stuff an NxN grid with the words chosen
# As much as possible we will try to link words together but we are lazy about
# it.

"""Create a new empty NxN wordsearch grid"""
new_grid = lambda N: [['' for i in range(N)] for j in range(N)]

def print_grid(g):
    print('-'*len(g))
    for r in g:
        for c in r:
            print(c,end='')
        print()

def merge_grids(g1, g2):
    for r in range(len(g1)):
        for c in range(len(g1)):
            if g2[r][c] is not '':
                g1[r][c] = g2[r][c]

def place_word(g, w, r, c, v):
    g2 = new_grid(len(g))
    if v:
        it = (1,0)
    else:
        it = (0,1)
    for ch in w:
        if g[r][c] is not '':
            return False
        if r >= len(g) or c >= len(g):
            return False
        g2[r][c] = ch
        r += it[0]
        c += it[1]
    merge_grids(g, g2)

g = new_grid(10)

place_word(g, chosen[0], 1, 1, True)

print_grid(g)
