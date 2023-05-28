def DataListInBit(data):
    dataBits = list(format(c, '08b') for c in bytearray(data.encode('latin-1')))
    return dataBits
print(DataListInBit('123'))