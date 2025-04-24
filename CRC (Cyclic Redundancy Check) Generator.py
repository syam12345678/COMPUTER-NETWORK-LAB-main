def xor(a, b):
    return ''.join(['0' if x == y else '1' for x, y in zip(a, b)])

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def encode_crc(data, key):
    appended_data = data + '0'*(len(key)-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

data = "100100"
key = "1101"
crc_code = encode_crc(data, key)
print("Original Data:", data)
print("CRC Codeword:", crc_code)
