from PIL import Image

def encrypt_image(image_path, output_path):
    """
    Encrypts the image by swapping pixel values and applying a basic mathematical operation.
    """
    image = Image.open(image_path)
    pixels = image.load()

    # Iterate through each pixel and swap RGB values
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            
            # Swap RGB values and apply a simple operation (adding 50 to each component)
            new_r = (r + 150) % 256
            new_g = (g + 150) % 256
            new_b = (b + 150) % 256
            
            # Assign the new encrypted pixel value
            pixels[x, y] = (new_r, new_g, new_b)

    # Save the encrypted image
    image.save(output_path)
    print(f"Encrypted image saved at: {output_path}")


def decrypt_image(image_path, output_path):
    """
    Decrypts the image by reversing the mathematical operation and swapping RGB values back.
    """
    image = Image.open(image_path)
    pixels = image.load()

    # Iterate through each pixel and reverse the operation (subtracting 50)
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            
            # Reverse the operation (subtract 50 from each component)
            new_r = (r - 150) % 256
            new_g = (g - 150) % 256
            new_b = (b - 150) % 256
            
            # Assign the new decrypted pixel value
            pixels[x, y] = (new_r, new_g, new_b)

    # Save the decrypted image
    image.save(output_path)
    print(f"Decrypted image saved at: {output_path}")


# Example usage:
encrypt_image('input_image1.jpeg', 'encrypted_image1.jpg')
decrypt_image('encrypted_image1.jpg', 'decrypted_image1.jpg')