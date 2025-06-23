
from PIL import Image
import traceback

try:
    print("Opening encrypted_image.png")
    enc_img = Image.open('encrypted_image.png')
    print("Encoded image opened successfully")

    # Load pixel values of the encoded image (RGB tuples)
    enc_pixelMap = enc_img.load()

    # Initialize variables for the hidden message
    msg = ""
    msg_index = 0

    print("Decoding message from image")
    # Traverse through the pixel values
    for row in range(enc_img.size[0]):
        for col in range(enc_img.size[1]):
            pixel = enc_pixelMap[row, col]
            r = pixel[0]  # R value

            if row == 0 and col == 0:
                msg_len = r
                print(f"Message length: {msg_len}")
            elif msg_index < msg_len:
                msg += chr(r)
                msg_index += 1

    print("Closing encoded image")
    enc_img.close()
    print("Image closed successfully")

    # Print the decoded message
    print("The hidden message is:\n")
    print(msg)

except Exception as e:
    print(f"An error occurred: {e}")
    print(traceback.format_exc())