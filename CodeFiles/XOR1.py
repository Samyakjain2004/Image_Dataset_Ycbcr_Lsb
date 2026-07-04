def xor_bits(bit1, bit2):
    return '1' if bit1 != bit2 else '0'

def xor_streams_bits(stream1, stream2):
    return ''.join(xor_bits(b1, b2) for b1, b2 in zip(stream1, stream2))

# Read the run-length encoded file, skipping spaces
with open(r"C:\Users\sudhanshu chaudhary\OneDrive\Desktop\YCBCR\runlength\final\xordecode2.txt", 'r') as f:
    encoded_data = f.read().replace(' ', '').strip()

# Read the processed map binary stream
with open('map.txt', 'r') as f:
    processed_map_stream = f.read().strip()

# Ensure both streams are of the same length
min_length = min(len(encoded_data), len(processed_map_stream))
encoded_data = encoded_data[:min_length]
processed_map_stream = processed_map_stream[:min_length]

# Perform XOR operation on each bit
xor_result_bits = xor_streams_bits(encoded_data, processed_map_stream)

# Output the result
xor_output_file = (r"C:\Users\sudhanshu chaudhary\OneDrive\Desktop\YCBCR\runlength\final\xordecode1.txt"
                   )
with open(xor_output_file, 'w') as f:
    f.write(xor_result_bits)

print(f'XOR result saved to {xor_output_file}')
