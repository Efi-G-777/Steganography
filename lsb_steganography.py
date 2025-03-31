def encode_image(image_path, text_path, output_path):
    # Ensure the image is converted to PNG format internally
    image = Image.open(image_path).convert("RGB")

    # Convert JPG to PNG before processing (to avoid compression issues)
    if image_path.lower().endswith(".jpg") or image_path.lower().endswith(".jpeg"):
        temp_png_path = image_path.rsplit(".", 1)[0] + ".png"
        image.save(temp_png_path, "PNG")
        image_path = temp_png_path  # Use converted PNG

    # Process as usual
    pixels = np.array(image)

    # Read the secret message
    with open(text_path, 'r') as file:
        secret_message = file.read()

    message_bits = text_to_bits(secret_message)
    message_length = len(message_bits)
    length_bits = format(message_length, '032b')  # Store length in first 32 bits
    full_bits = length_bits + message_bits

    height, width, _ = pixels.shape
    max_bits = height * width * 3

    if len(full_bits) > max_bits:
        raise ValueError("Message too large to hide in image")

    bit_index = 0
    for i in range(height):
        for j in range(width):
            for k in range(3):  # Iterate over R, G, B
                if bit_index < len(full_bits):
                    pixel_bin = format(pixels[i, j, k], '08b')
                    pixel_bin = pixel_bin[:-1] + full_bits[bit_index]
                    pixels[i, j, k] = int(pixel_bin, 2)
                    bit_index += 1

    encoded_image = Image.fromarray(pixels)
    encoded_image.save(output_path, "PNG")  # Always save as PNG to prevent loss
    print("Message successfully hidden in", output_path)