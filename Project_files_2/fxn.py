def func_compress(binary):
    binary = str(binary)
    res = ""
    i = 0
    while i < len(binary):
        if binary[i] == '1':
            res = res+binary[i]
            i = i+1
        else:
            c = 0
            while i < len(binary) and binary[i] == '0':
                c = c+1
                i = i+1
            if (c >= 1):
                c = c+1
                c = str(c)
                res = res+c
    return res

def func_restore(binary):
    i = 0
    res = ""
    while i < len(binary):
        if binary[i] == '1':
            res = res+binary[i]
            i = i+1

        else:
            n = int(binary[i])
            n = n-1
            while n > 0:
                res = res+'0'
                n = n-1
            i = i+1
    return res


# print(func_compress(10010))
# print(func_compress(111))
# print("hello")
# print(func_restore(func_compress(100010)))
# print(func_restore(func_compress(111)))
