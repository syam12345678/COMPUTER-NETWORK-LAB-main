def calc_parity(bits, positions):
    return sum(bits[pos - 1] for pos in positions) % 2

def encode_hamming(data_bits):
    d = [int(bit) for bit in data_bits]
    p1 = calc_parity(d, [0, 1, 3])
    p2 = calc_parity(d, [0, 2, 3])
    p3 = calc_parity(d, [1, 2, 3])
    return f"{p1}{p2}{d[0]}{p3}{d[1]}{d[2]}{d[3]}"
def detect_error(hamming_code):
    b = [int(bit) for bit in hamming_code]
    s1 = (b[0] + b[2] + b[4] + b[6]) % 2
    s2 = (b[1] + b[2] + b[5] + b[6]) % 2
    s3 = (b[3] + b[4] + b[5] + b[6]) % 2
    error_position = s1 + (s2 << 1) + (s3 << 2)
    return error_position
data = "1011"
encoded = encode_hamming(data)
print("Encoded Hamming Code:", encoded)
error_code = list(encoded)
error_code[2] = '1' if error_code[2] == '0' else '0'
error_code = ''.join(error_code)
print("With Error:", error_code)
pos = detect_error(error_code)
print("Error detected at position:", pos if pos != 0 else "No Error")
