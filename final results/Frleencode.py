

import cv2 as cv
import numpy as np

def save_run_length_to_file(encoded_data, file_path, bit_length):
    with open(file_path, 'w') as file:
        for value, count in encoded_data:
            padded_count = count.zfill(bit_length)
            file.write(f'{value}{padded_count}')

# Load image and convert to grayscale
img = cv.imread(r"C:\Users\sudhanshu chaudhary\OneDrive\Desktop\YCBCR\qrcode.png", cv.IMREAD_GRAYSCALE)
f_img = img.flatten()

final = []
prev_value = f_img[0]
count = 1

# Run-length encoding
for value in f_img[1:]:
    if prev_value == value:
        count += 1
    else:
        if prev_value == 255:
            prev_value = 1
        bin_count = bin(count)[2:]
        final.append((prev_value, bin_count))
        prev_value = value
        count = 1
if prev_value == 255:
    prev_value = 1
bin_count = bin(count)[2:]
final.append((prev_value, bin_count))

# Determine the maximum count value
max_count = max(int(count, 2) for _, count in final)
bit_length = max_count.bit_length()

# Calculate the total bits required
total_bits = sum(len(count.zfill(bit_length)) + 1 for _, count in final)  # +1 for the value bit

print('compressed', total_bits)
print('initial', img.shape[0] * img.shape[1])


# Save the encoded data to a file
save_run_length_to_file(final, r"C:\Users\sudhanshu chaudhary\OneDrive\Desktop\YCBCR\runlength\final\runlength_encoded.txt", bit_length)