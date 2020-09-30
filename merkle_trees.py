# https://nakamoto.com/merkle-trees/

from hashlib import sha1, sha256

def h(s): return sha1(s.encode()).hexdigest() # hashing helper function

block1 = "Block 1"
block2 = "Block 2"

digest1 = h(block1)
digest2 = h(block2)

root = h(digest1 + digest2)
print(root)

# 1. receive true merkle tree along with distro merkle tree
# 2. compare roots
# 3. if root does not equal then traverse distro merkle tree to find faulty node

### Assignment #2
# Given a string of a sentence as input, generate a Merkle tree whose blocks 
# are each word in the sentence (not including spaces, but including punctuation). 
# You will use SHA-2 as your hash function for this Merkle tree. Your function should
# take in a sentence as a string and return the Merkle root as a hex string.

import math

def sha2(s): return sha256(s.encode()).hexdigest()
def padds(n): return 2**(math.ceil(math.log2(n))) - n # returns number of padding needed to be power of 2

def merkleize(sentence: str) -> str:
    output = ""
    words = sentence.split(" ")
    print(words)

    for word in words:
        output += sha2(word)

    padding = padds(len(words))
    print(padding)

    for i in range(padding):
        output += chr(0)

    return sha2(output)

print(merkleize("I love chicken!"))
