
def brute_force_ceasar(cipher, alpha, sig):
    for key in range(1, len(alpha) + 1):
        m = ""
        for c in cipher:
            if c.lower() in alpha:
                index = ((alpha.find(c.lower()) + 1 - key) % len(alpha)) - 1
                m += alpha[index].lower() if c.islower() else alpha[index].upper()
            else:
                m += c
        if sig.upper() in m.upper():
            print("key: {}\nPlain text: {}".format(key, m))
            return
    print("Not found!!!")
    
brute_force_ceasar('SdepaDwp{g3i_yd@jd_d0_p3u}', 'abcdefghijklmnopqrstuvwxyz', 'WhiteHat{')