import cv2
import numpy as np
from scipy.stats import pearsonr

# Load the image
rgb_image = cv2.imread(r"C:\Users\sudhanshu chaudhary\OneDrive\Desktop\YCBCR\runlength\final\set of images\(256x256)image221.png")

# Convert the image from RGB to YCbCr
ycbcr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2YCrCb)

# Split the Y, Cb, Cr channels
Y_channel = ycbcr_image[:, :, 0]
Cb_channel = ycbcr_image[:, :, 1]
Cr_channel = ycbcr_image[:, :, 2]

# Flatten the Y channel for easier manipulation
y_flatten = Y_channel.flatten()

def read_binary_file(file_path):
    with open(file_path, 'r') as file:
        binary_string = file.read().strip()
    return binary_string

# Load the binary data to be embedded
file1 = r"C:\Users\sudhanshu chaudhary\OneDrive\Desktop\YCBCR\runlength\final\xorencode2.txt"
final = read_binary_file(file1)

def lsb_steganography(cover_frame, secret_message):
    stego_frame = cover_frame.copy()
    idx = 0
    for bit in secret_message:
        if bit in ['0', '1']:  # Only process valid bits
            x, y = idx % cover_frame.shape[1], idx // cover_frame.shape[1]
            if y >= cover_frame.shape[0]:
                break  # Prevent overflow
            pixel = stego_frame[y, x]
            pixel = (pixel & ~1) | int(bit)
            stego_frame[y, x] = pixel
            idx += 1
    return stego_frame

# Apply LSB steganography to the Y channel
Y_channel_stego = lsb_steganography(Y_channel, final)

# Merge the modified Y channel back with the original Cb and Cr channels
embycrcb = cv2.merge((Y_channel_stego, Cb_channel, Cr_channel))

# Convert the modified YCbCr image back to RGB
rgbemb = cv2.cvtColor(embycrcb, cv2.COLOR_YCrCb2RGB)

# Save the modified image
save_path = r"C:\Users\sudhanshu chaudhary\OneDrive\Desktop\YCBCR\runlength\final\encrypted_image.png"
cv2.imwrite(save_path, rgbemb)

# Compute PSNR between the original and modified images
def compute_psnr(original, modified):
    mse = np.mean((original - modified) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

psnr = compute_psnr(rgb_image, rgbemb)
print("PSNR:", psnr)

# Compute correlation between the original and modified images
def compute_correlation(original, modified):
    original_flat = original.flatten()
    modified_flat = modified.flatten()
    correlation, _ = pearsonr(original_flat, modified_flat)
    return correlation

corr = compute_correlation(rgb_image, rgbemb)
print("Correlation:", corr)
