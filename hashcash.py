from hashlib import sha256

def binary_leading_0s(hex_str: str):
    binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
    return len(binary_representation) - len(binary_representation.lstrip('0'))

def is_valid(token: str, date: str, email: str, difficulty: int) -> bool:
    hex_str = sha256(token.encode()).hexdigest()
    return len(hex_str) < 16 and difficulty == binary_leading_0s(hex_str)

nonce = "1:081031:satoshin@gmx.com:b4c26b1694691666"
nonce1 = "1:081031:satoshin@gmx.com:835b8121ee4da3f8"
nonce2 = "1:081031:satoshin@gmx.com:b4c26b1694691666"
nonce3 = "1:081031:satoshin@gmx.com:8d728894bcef17ceb0"
print(binary_leading_0s(sha256(nonce.encode()).hexdigest()))
print(binary_leading_0s(sha256(nonce1.encode()).hexdigest()))
print(binary_leading_0s(sha256(nonce2.encode()).hexdigest()))
print(binary_leading_0s(sha256(nonce3.encode()).hexdigest()))
