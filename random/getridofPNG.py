import os

def remove_png_from_txt_filenames(base_dir, extension=".PNG"):
    # Traverse all subdirectories in the base directory
    for subdir, _, files in os.walk(base_dir):
        for file in files:
            # Process only .txt files
            if file.endswith('.txt'):
                # Check if the filename ends with '.PNG.txt'
                if file.endswith(f'{extension}.txt'):
                    # Create the new filename by removing the .PNG part
                    new_filename = file.replace(f'{extension}.txt', '.txt')
                    old_txt_file_path = os.path.join(subdir, file)
                    new_txt_file_path = os.path.join(subdir, new_filename)
                    
                    # Rename the file if the new filename is different
                    if old_txt_file_path != new_txt_file_path:
                        os.rename(old_txt_file_path, new_txt_file_path)
                        print(f"Renamed: {old_txt_file_path} -> {new_txt_file_path}")

if __name__ == '__main__':
    base_directory = '/home/user/Documents/MISC_code/order/train'  # Replace with the path to your base directory
    remove_png_from_txt_filenames(base_directory)

