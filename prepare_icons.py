import requests
from PIL import Image
from io import BytesIO
import os

def download_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

def main():
    os.makedirs('build', exist_ok=True)
    os.makedirs('public', exist_ok=True)

    # Logo
    logo = download_image('https://midasteknoloji.com/wp-content/uploads/2022/09/logo.png')
    logo.save('public/logo.png')

    # Favicon (square)
    fav = download_image('https://midasteknoloji.com/wp-content/uploads/2022/09/cropped-favicon.png')
    fav = fav.convert("RGBA")
    
    # Save sizes
    fav.resize((512, 512)).save('build/icon.png')
    
    # Save proper ICO with multiple sizes
    icon_sizes = [(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]
    fav.save('build/icon.ico', format='ICO', sizes=icon_sizes)
    fav.save('public/favicon.ico', format='ICO', sizes=icon_sizes)
    
    fav.resize((512, 512)).save('public/pwa-512x512.png')
    fav.resize((192, 192)).save('public/pwa-192x192.png')
    fav.resize((180, 180)).save('public/apple-touch-icon-180x180.png')
    fav.resize((32, 32)).save('public/favicon.png')
    
    print("Images prepared successfully!")

if __name__ == '__main__':
    main()
