import base64

c = "NFwcKxN4DxMGLVxFABUAADgQFgAqMgNRMQ89PAAbNyldXg4iF1xBJik=".encode()

b64_dcode = base64.b64decode(c)

flag = "WhiteHat{"

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

key = xor(b64_dcode, flag.encode())

flag = xor(key * (len(b64_dcode) // len(key)), b64_dcode) + key
print(flag.decode())