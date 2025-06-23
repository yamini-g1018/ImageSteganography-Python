
from PIL import Image
import traceback

try:
    print("Opening original_image.png")
    org_img = Image.open('original_image.png')
    print("Original image opened successfully")

    # Load pixel values of the original image (RGB tuples)
    org_pixelMap = org_img.load()

    print("Creating new image")
    enc_img = Image.new(org_img.mode, org_img.size)
    enc_pixelsMap = enc_img.load()
    print("New image created")

    # Read message to be encrypted from user
    msg = input("Enter the message: ")
    msg_index = 1  # Start at 1 since first pixel stores message length

    # Get the length of the message
    msg_len = len(msg)
    print(f"Message length: {msg_len}")

    # Check if image has enough pixels
    if msg_len > (org_img.size[0] * org_img.size[1] - 1):
        raise ValueError("Message too long for image size")

    print("Encoding message into image")
    # Traverse through the pixel values
    for row in range(org_img.size[0]):
        for col in range(org_img.size[1]):
            r, g, b = org_pixelMap[row, col]
            
            if row == 0 and col == 0:
                enc_pixelsMap[row, col] = (msg_len, g, b)
            elif msg_index <= msg_len:
                ascii = ord(msg[msg_index - 1])
                enc_pixelsMap[row, col] = (ascii, g, b)
                msg_index += 1
            else:
                enc_pixelsMap[row, col] = (r, g, b)

    print("Saving encoded image")
    enc_img.save("encrypted_image.png")
    print("Encoded image saved as encrypted_image.png")

    # Display the encoded image
    print("Displaying encoded image")
    enc_img.show()

    # Close images
    print("Closing images")
    org_img.close()
    enc_img.close()
    print("Images closed successfully")

except Exception as e:
    print(f"An error occurred: {e}")
    print(traceback.format_exc())
