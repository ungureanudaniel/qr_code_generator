import string
import random
from urllib.request import urlopen

import segno

# ----------generate unique code--------------------
def qr_nr(length: int) -> str:
    """
    Generate a unique random code consisting of letters.
    
    Args:
        length (int): Length of the generated code.
    
    Returns:
        str: A random string of letters.
    """
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

# ----------generate qr code--------------------
def generate_qr(url: str, location: str, extension: str, scale: int, border: int) -> None:
    """
    Generate a QR code for the given URL and save it as a file with a unique name.
    
    Args:
        url (str): The URL to encode in the QR code.
        location (str): The directory and base name for the saved QR code file.
        extension (str): File extension (e.g., 'svg', 'png').
        scale (int): The scaling factor for the QR code.
        border (int): The border size for the QR code.
    """
    qrcode = segno.make_qr(url, error='h')
    filename = f"{location}{qr_nr(4)}.{extension}"
    qrcode.save(filename, scale=scale, border=border)


if __name__ == "__main__":
    try:
        url = 'https://bucegipark.ro/ro/education/bear-awareness'
        location = 'generated_qr/basic_qrcode_'
        extension = 'svg'
        scale = 5
        border = 1
        generate_qr(url, location, extension, scale, border)
    except Exception as e:
        print(f"Error: {e}")