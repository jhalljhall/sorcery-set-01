import os
import json
import requests

def download_image(image_url, folder_path, file_name):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_path = os.path.join(folder_path, file_name)
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"Image downloaded: {file_name}")
    else:
        print(f"Failed to download image: {image_url}")

def main():
    # Load the JSON data from "cards.json"
    with open("alpha_cards_list.json", "r") as json_file:
        data = json.load(json_file)

    # Create the "cards" folder if it doesn't exist
    folder_path = "alphaclash_cards"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Loop through the data array and download the images
    for item in data["data"]:
        image_url = item["imageUrl"]
        file_name = f"{item['slug']}.webp"
        download_image(image_url, folder_path, file_name)

if __name__ == "__main__":
    main()