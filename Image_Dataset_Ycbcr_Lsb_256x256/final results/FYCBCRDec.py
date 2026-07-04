import cv2
import numpy as np

# Load the modified image
modified_rgb_image = cv2.imread(r"C:\Users\sudhanshu chaudhary\OneDrive\Desktop\YCBCR\runlength\final\encrypted_image.png")

# Convert the image from RGB to YCbCr
modified_ycbcr_image = cv2.cvtColor(modified_rgb_image, cv2.COLOR_RGB2YCrCb)

# Extract the Y channel
modified_Y_channel = modified_ycbcr_image[:, :, 0]

# Flatten the Y channel for easier manipulation
modified_y_flatten = modified_Y_channel.flatten()

# Function to extract a specific number of LSBs from the modified Y channel
def extract_lsb(modified_flatten, num_bits):
    extracted_bits = []
    for i in range(num_bits):
        extracted_bit = modified_flatten[i] & 1  # Extract the LSB
        extracted_bits.append(str(extracted_bit))
    return ''.join(extracted_bits)

# Extract the first 50,115 bits of hidden binary data
num_bits_to_extract = 50115
extracted_data = extract_lsb(modified_y_flatten, num_bits_to_extract)

# Save the extracted data to a file
extracted_data_path = r"C:\Users\sudhanshu chaudhary\OneDrive\Desktop\YCBCR\runlength\final\extracted_bits.txt"
with open(extracted_data_path, 'w') as file:
    file.write(extracted_data)

print("Extraction complete. Data saved to", extracted_data_path)
