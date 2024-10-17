from PIL import Image
def bin_to_str(binary_data):
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    data = ''.join([chr(int(byte, 2)) for byte in all_bytes])
    return data

def bin32_to_int(b):
    return int(b, 2)
def decode(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = image.load()
    binary_data = ''
    idx = 0
    data_len = None
    total_bits = image.width * image.height * 1
    for y in range(image.height):
        for x in range(image.width):
            if idx >= total_bits:
                break
            r, g, b = pixels[x, y]
            lsb = r & 1
            if idx < 32:
                binary_data += str(lsb)
                if idx == 31:
                    data_len = bin32_to_int(binary_data)
                    binary_data = ''
            elif data_len is not None and idx < 32 + data_len:
                binary_data += str(lsb)
                if idx == 32 + data_len - 1:
                    break
            idx += 1
        else:
            continue
        break
    data = bin_to_str(binary_data)
    print("Encoded Data:", data)

if __name__ == "__main__":
    image_path = 'encoded_image.png'
    decode(image_path)
