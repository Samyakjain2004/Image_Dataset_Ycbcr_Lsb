import cv2 as cv
import numpy as np

def extract_first_bits(binary_string, bit_count):
    # Extract the first bit_count bits from the binary string
    return binary_string[:bit_count]


def decode_run_length(encoded_file, bit_length, bit_count):
    with open(encoded_file, 'r') as file:
        binary_string = file.read().strip()

    # Extract only the first bit_count bits
    binary_string = extract_first_bits(binary_string, bit_count)


    pixels = []
    i = 0
    while i < len(binary_string):
        pixel_value = int(binary_string[i])
        pixel_intensity = 255 if pixel_value == 1 else 0
        count = int(binary_string[i + 1:i + 1 + bit_length], 2)
        pixels.extend([pixel_intensity] * count)
        i += 1 + bit_length

    return pixels


def display_image(decoded_pixels, original_shape):
    total_pixels = np.prod(original_shape)

    # Ensure the number of pixels matches the original shape
    if len(decoded_pixels) > total_pixels:
        decoded_pixels = decoded_pixels[:total_pixels]
    elif len(decoded_pixels) < total_pixels:
        # If there are fewer pixels, pad with 0 (black)
        decoded_pixels.extend([0] * (total_pixels - len(decoded_pixels)))

    pixel_array = np.array(decoded_pixels, dtype=np.uint8)
    image_array = pixel_array.reshape(original_shape)
    cv.imshow('Decoded Image', image_array)
    cv.waitKey(0)
    cv.destroyAllWindows()


# Example usage
bit_length = 14  # Adjust this to match your encoding bit length
encoded_file = r"C:\Users\sudhanshu chaudhary\OneDrive\Desktop\YCBCR\runlength\final\xordecode1.txt"
bit_count = 50115  # Number of bits to extract before decoding
original_shape = (330, 330)  # Replace with your image dimensions

decoded_pixels = decode_run_length(encoded_file, bit_length, bit_count)
display_image(decoded_pixels, original_shape)