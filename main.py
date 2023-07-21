import os
from PIL import Image

def convert_webp_to_png(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".webp"):
            webp_path = os.path.join(folder_path, filename)
            png_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.png")
            try:
                im = Image.open(webp_path)
                im.save(png_path)
                print(f"Converted {filename} to {os.path.basename(png_path)}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

def main():
    folder_path = "alphaclash_cards"  # Change this to the path of your folder containing .webp files
    convert_webp_to_png(folder_path)

if __name__ == "__main__":
    main()
