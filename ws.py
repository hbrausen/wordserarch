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


