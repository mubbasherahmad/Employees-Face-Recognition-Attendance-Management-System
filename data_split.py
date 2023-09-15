
    # Your splitting and copying code here...
import os
import random
import shutil
from sklearn.model_selection import train_test_split

# Define paths to your original dataset directory
original_data_dir = 'D:\Bushi\Dummy of Project\Datasets'

# Define paths to your new train, validation, and test data directories
train_data_dir = 'train'
validation_data_dir = 'validation'
test_data_dir = 'test'

# List all subdirectories (classes) in the original data directory
class_names = os.listdir("D:\Bushi\Dummy of Project\Datasets")

# Set random seed for reproducibility
random.seed(42)

# Create train, validation, and test directories for each class
for class_name in class_names:
    class_dir = os.path.join(original_data_dir, class_name)
    print("1st",class_dir)
    
    train_class_dir = os.path.join(original_data_dir,train_data_dir, class_name)
    print("2st",train_class_dir)
    validation_class_dir = os.path.join(original_data_dir,validation_data_dir, class_name)
    print("3st",validation_class_dir)
    test_class_dir = os.path.join(original_data_dir,test_data_dir, class_name)
    print("4st",test_class_dir)
    #os.makedirs(class_dir,exist_ok=True)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(validation_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)
    
    # List all images in the class directory
    all_images = os.listdir(class_dir)
    
    # Shuffle the images randomly
    random.shuffle(all_images)
    
    # Split data into train, validation, and test sets
    train_images, test_images = train_test_split(all_images, test_size=0.2, random_state=42)
    train_images, validation_images = train_test_split(train_images, test_size=0.2, random_state=42)
    
    # Copy images to respective directories
    def copy_images(images, source_dir, dest_dir):
        for image in images:
            src_path = os.path.join(source_dir, image)
            dest_path = os.path.join(dest_dir, image)
            shutil.copy(src_path, dest_path)
    
    copy_images(train_images, class_dir, train_class_dir)
    copy_images(validation_images, class_dir, validation_class_dir)
    copy_images(test_images, class_dir, test_class_dir)
