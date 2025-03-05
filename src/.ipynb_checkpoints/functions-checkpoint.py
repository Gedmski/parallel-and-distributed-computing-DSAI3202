import glob
import cv2
import time
from skimage.filters.rank import entropy
from skimage.morphology import disk
from scipy import ndimage as nd
from skimage.filters import sobel, gabor, hessian, prewitt
import matplotlib.pyplot as plt
from tqdm import tqdm
import multiprocessing as mp

def read_images(images_path):
    """
    Reads all images from a specified path using OpenCV.

    Parameters:
        - images_path (str): The path to the directory containing the images.
    Returns:
        - images (list): A list of images read from the directory.
    """
    images = []
    for file_path in images_path:
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
                images.append(image)
    return images


def execution():
    # Define the path to the dataset
    dataset_path = '../data/brain_tumor_dataset/'
    
    # List all image files in the 'yes' and 'no' directories
    yes_images = glob.glob(dataset_path + 'yes/*.jpg')
    no_images = glob.glob(dataset_path + 'no/*.jpg')
    
    yes_images = read_images(yes_images)
    no_images = read_images(no_images)
    
    print(f"Number of 'yes' images: {len(yes_images)}")
    print(f"Number of 'no' images: {len(no_images)}")