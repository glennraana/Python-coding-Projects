from PIL import Image
import pyheif
import os

# Folder paths
input_folder = "/Users/glenn/make_dataset/glasses"
output_folder = "/Users/glenn/make_dataset/converted_pictures"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop over all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".heic"):
        heic_path = os.path.join(input_folder, filename)
        jpg_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")

        # Convert HEIC to JPG using pyheif and Pillow
        try:
            heif_file = pyheif.read(heic_path)
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data, 
                "raw", 
                heif_file.mode, 
                heif_file.stride
            )
            image.save(jpg_path, "JPEG")
            print(f"Converted {filename} to JPG")
        except Exception as e:
            print(f"Error converting {filename}: {e}")

print("Conversion complete!")



