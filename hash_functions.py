from hashlib import md5
from random import randint

def md125(s: str) -> str: # use this hash function to generate a collision
  return md5(s.encode()).hexdigest()[:8]

def generate_md125_collisions() -> (str, str):
  preimages = {}
  msg = "nakamotoa"
  while True:
    my_hash = md125(msg)
    if my_hash in preimages:
      print(f"{hash}: {preimages[my_hash]}, {msg}")
    preimages[my_hash] = msg
    msg += 1

# resources:
# https://crypto.stackexchange.com/questions/34585/is-it-possible-to-brute-force-a-hash-algorithm-of-32-bits
# https://github.com/thereal1024/python-md5-collision/blob/master/coll.py
# https://github.com/thereal1024/python-md5-collision/blob/master/gen_coll_python.py
