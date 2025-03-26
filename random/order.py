import os
import re
import shutil

def rename_and_move_images_and_labels(base_dir):
    # Create directories to store renamed images and labels
    new_images_dir = os.path.join(base_dir, 'renamed_images')  # Directory to store renamed images
    new_labels_dir = os.path.join(base_dir, 'renamed_labels')  # Directory to store renamed labels
    
    os.makedirs(new_images_dir, exist_ok=True)
    os.makedirs(new_labels_dir, exist_ok=True)

    # Initialize a counter for the frame numbers
    frame_counter = 1

    # Loop through each directory in the base directory (subdirectories containing images and labels)
    for subdir_name in os.listdir(base_dir):
        subdir_path = os.path.join(base_dir, subdir_name)
        
        # Check if it's a directory
        if os.path.isdir(subdir_path):
            images_dir = os.path.join(subdir_path, 'images', 'train')
            labels_dir = os.path.join(subdir_path, 'labels', 'train')
            
            # Skip if either images or labels directory doesn't exist in this subdirectory
            if not os.path.exists(images_dir) or not os.path.exists(labels_dir):
                continue

            # Get all image files and sort them (assuming the filenames contain numbers for sorting)
            image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg', '.gif'))]
            image_files.sort(key=lambda x: int(re.search(r'(\d+)', x).group()) if re.search(r'(\d+)', x) else 0)

            # Process images and labels
            for image_file in image_files:
                # Generate new image name
                new_image_name = f"frame_{frame_counter:06d}{os.path.splitext(image_file)[1]}"
                old_image_path = os.path.join(images_dir, image_file)
                new_image_path = os.path.join(new_images_dir, new_image_name)

                # Rename and move the image
                shutil.copy2(old_image_path, new_image_path)  # Use copy2 to preserve metadata
                
                # Corresponding label file (assuming the label has the same name as the image but with .txt extension)
                label_name = os.path.splitext(image_file)[0] + '.txt'
                old_label_path = os.path.join(labels_dir, label_name)
                
                # If the label file exists, rename and move it
                if os.path.exists(old_label_path):
                    new_label_name = f"{new_image_name}.txt"
                    new_label_path = os.path.join(new_labels_dir, new_label_name)
                    shutil.copy2(old_label_path, new_label_path)  # Copy the label to the new directory

                # Increment the frame counter for the next image
                frame_counter += 1

if __name__ == '__main__':
    base_directory = '/home/user/Documents/MISC_code/order'  # Replace with the path to your base directory
    rename_and_move_images_and_labels(base_directory)

