import os
import shutil

def copy_images(src_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate through all subdirectories and files in the source directory
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            print(f"filename: {file}")
            # Check if the file has an image extension
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                # Build the source and destination file paths
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)

                # Copy the file to the destination directory
                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied: {src_file_path} to {dest_file_path}")

# Example usage
source_directory = "./Sick"
destination_directory = "./Thermography-image-data/Sick"



copy_images(source_directory, destination_directory)