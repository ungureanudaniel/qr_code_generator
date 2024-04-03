import segno
import random
import string
from PIL import Image
from urllib.request import urlopen
# #----------generate unique code--------------------
def qr_nr(y):
    
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def generate_qr(url: string, location:string,extension:string, scale:int, border:int):
    # Generate the QR code
    qrcode = segno.make_qr(url)

    # Save the QR code with a unique filename
    filename = f"{location}{qr_nr(4)}.{extension}"
    qrcode.save(filename, scale=scale, border=border)

    # Add logo to the QR code image if logo_path is provided
    # if logo_path:
    #     qr_image = Image.open(filename)
    #     logo_image = Image.open(logo_path)

    #     # Calculate the position to place the logo at the center of the QR code image
    #     position = ((qr_image.size[0] - logo_image.size[0]) // 2, (qr_image.size[1] - logo_image.size[1]) // 2)

    #     # Paste the logo onto the QR code image
    #     # qr_image.paste(logo_image, position, logo_image)

        # Save the image with the logo

if __name__=="__main__":
    # Load your brand logo image
    try:
        # logo_path = "C:/Users/PNB-IT/Documents/code/qrcodes/logo/bucegi_logo.png"
        url = input("Enter the URL: ")
        location = input("Enter the location to save the QR code (e.g., 'generated_qr/basic_qrcode_'): ") or "generated_qr/basic_qrcode_"
        extension = input("Enter the file extension (e.g., 'png'): ") or 'png'
        scale = int(input("Enter the scale (e.g., 5): ")) 
        border = int(input("Enter the border width (e.g., 1): "))
        generate_qr(url, location, extension, scale, border)
    except Exception as e:
        print(f'Error! {e}')
