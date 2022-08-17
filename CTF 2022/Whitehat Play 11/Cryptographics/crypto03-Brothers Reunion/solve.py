import string
import base64
import binascii


cipher = '78 6 1 65 0 57 1 78 0 28 1 99 0 23 1 78 0 9 1 2 1 33 1 78 0 6 1 81 0 39 1 78 0 9 1 2 1 50 0 40 1 16 1 82 0 25 1 77 0 45 1 103 0 49 0 41 1 16 1 77 0 42 1 78 0 6 1 23 1 15 1 79 0 5 1 77 0 50 0 28 1 28 1 1 1 15 1 79 0 68 0 31 1 53 0 25 1 9 1 2 1 49 0 29 1 44 1 77 0 50 0 27 1 45 1 107 0 50 0 29 1 5 1 77 0 52 0 52'

cipher = cipher.split()

def show(cipher, secret):
    result = ""
    for i in range(len(cipher)):
        char = cipher[i]
        if (char.isupper()):
            result += chr((ord(char) - pow(-1,i) * secret - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) - pow(-1,i) * secret - 97) % 26 + 97)
        elif (char.isdecimal()):
            result += chr((ord(char) - pow(-1,i) * secret - 48) % 10 + 48)
        else:
            result += char
    return result

def de_stuff(cipher):
    alpha_b64 = [ord(c) for c in (string.ascii_letters + string.digits + "+/=")]

    a = int(cipher[0])
    data = [a]
    # stuff:
    # (b % a), (b // a), (c % b), (c // b), (d % c), (d // c)
    # de_stuff:
    for i in range(1, len(cipher) - 1, 2):
        Mod = int(cipher[i])
        Div = int(cipher[i + 1])

        for b in alpha_b64:
            if b % a == Mod and b // a == Div:
                a = b
                break
        
        data.append(a)

    result = "".join([chr(c) for c in data])
    newtext = base64.b64decode(result).decode('ascii')
    return binascii.unhexlify(newtext).decode('ascii')


if __name__ == "__main__":
    mess_hide = de_stuff(cipher)
    print("[+] Flag: WhiteHat{%s}" % show(mess_hide, 5))