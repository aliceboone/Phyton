'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded
back to original list of strings. Please inplement encode and decode

Input = ["lint", "code", "love", "you"]
Output = ["lint", "code", "love", "you"]
one possible encode method eis: "lint:;code:;loce:;you"

'''
def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

print(encode(["lint", "code", "love", "you"]))

def decode(s):
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return res

print(decode("4#lint4#code4#love3#you"))







