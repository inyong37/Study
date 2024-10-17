# 1. Connect to Google Drive
# Mount Google Drive to save the image
from google.colab import drive
drive.mount('/content/drive')

# 2. Download and save the image
import requests

# URL of the image you want to download
image_url = 'https://your_image_link_here.webp'

# Path to save the image in Google Drive
save_path = '/content/drive/My Drive/your_folder_name/your_image_name.webp'

# Send a GET request to download the image
response = requests.get(image_url)

# Save the image to Google Drive
with open(save_path, 'wb') as file:
    file.write(response.content)

print(f"Image saved to: {save_path}")
