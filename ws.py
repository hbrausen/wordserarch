import random
import re

"""Import list of words from english wordlist"""
def import_wordlist():
    return [w for w in open("words_mit.txt",'r').readlines()]

"""Filter out any words that contain numbers"""
def filter_out_nums(word):
    for c in word:
        if c in '1234567890':
            return False
    return True

"""Filter out words beyond a certain length"""
def filter_beyond_len(n):
    return lambda w: len(w) <= n

def filter_less_than_len(n):
    return lambda w: len(w) >= n

wl = import_wordlist()

# Just deal with the "real" words for now and trim ws
wl = list(map(lambda s: s.strip(),filter(filter_out_nums, wl)))

# Filter out non alphanumeric characters
p = re.compile('^[a-zA-Z]*$')
wl = [w for w in wl if p.match(w)]

# Next, trim down to words less than a certain length
wl = list(filter(filter_beyond_len(10), wl))

# Next, trim down to words more than a certain length
wl = list(filter(filter_less_than_len(3), wl))

# Make them all lowercase
chosen = [w.lower() for w in wl]

# Now we have our words for the wordsearch selected
# The next step is to lay them out in a grid
# This is the hard part
# We will set a target wordsearch puzzle dimension N
# and then attempt to stuff an NxN grid with the words chosen
# As much as possible we will try to link words together but we are lazy about
# it.

"""Create a new empty NxN wordsearch grid"""
new_grid = lambda N: [[' ' for i in range(N)] for j in range(N)]

def print_grid(g):
    print('-'*(2+len(g)))
    for r in g:
        print('|',end='')
        for c in r:
            print(c,end='')
        print('|')
    print('-'*(2+len(g)))

def merge_grids(g1, g2):
    g = new_grid(len(g1))
    for r in range(len(g1)):
        for c in range(len(g1)):
            # Try to pluck character from g2
            if g2[r][c] != ' ':
                if g1[r][c] in (' ', g2[r][c]):
                    g[r][c] = g2[r][c]
            # Otherwise pluck from g1
            else:
                g[r][c] = g1[r][c]
    return g

def place_word(g, w, r, c, v):
    g2 = new_grid(len(g))
    if v:
        it = (1,0)
    else:
        it = (0,1)
    for ch in w:
        if r >= len(g) or c >= len(g):
            return None
        if g[r][c] not in (' ', ch):
            return None
        g2[r][c] = ch
        r += it[0]
        c += it[1]
    return merge_grids(g, g2)

def fill_empty(g):
    for r in range(len(g)):
        for c in range(len(g)):
            if g[r][c] == ' ':
                g[r][c] = random.choice('abcdefghijklmnopqrstuvwxyz')

N = 10

g = new_grid(N)

words = []
for i in range(20):
    word = random.choice(chosen)
    ret = place_word(g, word, random.randint(0,N-1), random.randint(0,N-1),
                     bool(random.getrandbits(1)))
    if ret is not None:
        g = ret
        words += [word]
fill_empty(g)
print_grid(g)
for word in words:
    print(word)
