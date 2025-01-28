Image Encryption Tool

This project is a simple Python-based tool that lets you encrypt images by modifying their pixel values. It applies techniques like swapping pixel values or using mathematical transformations to change the appearance of an image, making it unrecognizable.

Features

Pixel Swapping: Reorganizes pixel values within an image to scramble it.

Mathematical Transformations: Alters pixel brightness or color by applying simple math (e.g., adding or subtracting values).
These operations ensure the image is encrypted but can still be processed further for custom needs.

Requirements
To run the tool, you’ll need:

Python installed on your system.
Two libraries:
Pillow: For image handling.
Numpy: For efficient pixel manipulation.

How It Works?
You provide an input image (e.g., a photo you want to encrypt).
The tool modifies the pixel data using one of the following methods:
Swapping: Changes the positions of certain pixels.
Math Operations: Adjusts pixel values by adding or subtracting numbers.
The modified (encrypted) image is saved as a new file.


Steps to Use
Place your input image (e.g., my_photo.jpg) in the project folder.
Edit the script to include your input and output file names (e.g., input_image.jpg and encrypted_image.jpg).
Run the script, and it will create an encrypted version of your image.
Input and Output
Input: A clear and normal image.
Output: An encrypted, scrambled version of the image.
Why Use It?
This tool is perfect for:

Learning about image encryption basics.
Experimenting with pixel-level transformations.
Protecting sensitive visual data in a basic way.

