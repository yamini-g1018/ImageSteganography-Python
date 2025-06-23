# ImageSteganography 
 
A Python project to hide text messages in PNG images using steganography by modifying the red channel of pixels and extract them later. Includes scripts to encode, decode, and generate a sample wavy rainbow `original_image.png`. 
 
## Features 
- Hide text in PNG images without visible changes. 
- Extract hidden messages accurately. 
- Generate a 200x200 sample image for testing. 
 
## Files 
- `encoder.py`: Hides text in `original_image.png`, outputs `encrypted_image.png`. 
- `decoder.py`: Extracts text from `encrypted_image.png`. 
- `create_new_original_image.py`: Creates a wavy rainbow `original_image.png`. 
- `original_image.png`: Sample input image. 
 
## Requirements 
- Python 3.6+ 
- Pillow (`pip install Pillow`) 
 
## Usage 
1. Run `python create_new_original_image.py` to generate `original_image.png`. 
2. Run `python encoder.py`, enter a message (e.g., `RainbowSecret2025`). 
3. Run `python decoder.py` to view the hidden message. 
