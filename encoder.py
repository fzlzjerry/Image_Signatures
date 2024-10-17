from PIL import Image
import datetime

def str_to_bin(data):
    return ''.join(format(ord(i), '08b') for i in data)

def int_to_bin32(n):
    return format(n, '032b')

def encode(image_path, output_path, data):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = image.load()
    binary_data = str_to_bin(data)
    data_len = len(binary_data)
    data_len_bin = int_to_bin32(data_len)
    total_data = data_len_bin + binary_data
    idx = 0
    for y in range(image.height):
        for x in range(image.width):
            if idx < len(total_data):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(total_data[idx])
                pixels[x, y] = (r, g, b)
                idx += 1
            else:
                break
        if idx >= len(total_data):
            break
    if idx < len(total_data):
        print("Error: Data is too large to encode in the image.")
        return
    image.save(output_path)
    print("Data encoded successfully.")

if __name__ == "__main__":
    image_path = 'input_image.png'
    output_path = 'encoded_image.png'
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = 'Morax Cheng ' + current_datetime
    encode(image_path, output_path, data)
