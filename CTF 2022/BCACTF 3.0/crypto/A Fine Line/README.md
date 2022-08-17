# A Fine Line
175 points - By Marvin

Tag: crypto

I'm carefully drawing a fine line on this piece of paper, letting each portion guide the next... (Digits and letters are 0-9 and 10-35 in their usual orders, and the underscore is 36. {} are not encoded but should be added in afterwards. All letters are lowercase.)

[chall.txt](chall.txt)

## Hint
- This uses the affine cipher, as clued by the title and description, but with an added modification.
- Each pair of letters decodes the next.

## Write up

1. Learn about Affine cryptography first. The input is a character $c$ and the key pair $a$ and $b$. With $a, b, c \in Z_{n}$. The encryption and decryption formula can be seen below:

$E(c) = x = (ac + b) \mod n$

$D(x) = a^{-1}(x - b) \mod n$

Decode each character and combine them to produce plaintext.

``` python3
from Crypto.Util.number import inverse
import string
ALPHA = string.digits + string.ascii_lowercase + "_"

def dcode_affine_cipher(message, key):
    translated = '' 
    modInverseOfKeyA = inverse(key[0], len(ALPHA))
    for symbol in message:
        symIndex = ALPHA.find(symbol)
        translated += ALPHA[(symIndex - key[1]) * modInverseOfKeyA % len(ALPHA)]

    return translated
```

1. Now we have a ceramic alphabet with digits, lowercase and underscore (This is episode $Z_{n}$ with $n = 37$). From the hint we can guess that we will use the previously decoded character pair to solve the following pair of characters. For example, `bc` will be used as key pairs. With $a = 1$ and $b = 2$ (index of `bc` characters in the alphabet). Then use the newly earned key pair to decode the next letter pair (hint) => D(`bx`) = `ac`. Do the same goes for the rest of the cipher.

``` python3
pair_letters_curr = 'bc'
cipher = 'bx6ez_unufi3bm0r0xeb'
flag = pair_letters_curr
for i in range(0, len(cipher), 2):
    pair_letters_cipher = cipher[i : i + 2]
   
    a = ALPHA.index(pair_letters_curr[0])
    b = ALPHA.index(pair_letters_curr[1])
    pair_letters_curr = dcode_affine_cipher(pair_letters_cipher, (a, b))
    flag += pair_letters_curr

flag = flag[:6] + '{' + flag[6:]+ "}"
print(flag)
```

Flag: `bcactf{g2b_npjs3p4d65k1}`