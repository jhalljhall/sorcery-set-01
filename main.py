import os
import requests

# Function to download the image from a given URL and save it to the current directory
def download_image(url, image_name):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(image_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    else:
        print(f"Failed to download image {image_name} from URL: {url}")
        return False

# Loop from 1 to 402 and replace the string "{{replaceme}}" with the loop index
for i in range(141, 403):
    image_name = f"{i:03}.png"
    url = f"https://curiosa.io/_next/image?url=https://d27a44hjr9gen3.cloudfront.net/alp/{image_name}&w=640&q=75"
    
    # Download the image and copy it to the current directory
    if download_image(url, image_name):
        print(f"Image {image_name} downloaded successfully from URL: {url}")
    else:
        print(f"Image {image_name} download failed from URL: {url}")

