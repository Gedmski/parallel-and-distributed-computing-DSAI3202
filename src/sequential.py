import time
from tqdm import tqdm
from skimage.filters.rank import entropy
from skimage.morphology import disk
from scipy import ndimage as nd
from skimage.filters import sobel, gabor, hessian, prewitt

def process_images(images):
    processed_images = []
    for image in tqdm(images[:]):
        filtered_images = {
            'Original': image,
            'Entropy': entropy(image, disk(2)),
            'Gaussian': nd.gaussian_filter(image, sigma=1),
            'Sobel': sobel(image),
            'Gabor': gabor(image, frequency=0.9)[1],
            'Hessian': hessian(image, sigmas=range(1, 100, 1)),
            'Prewitt': prewitt(image)
        }
        processed_images.append(filtered_images)
    return processed_images

def execution(yes_images, no_images):
    start_time = time.time()
    yes_inputs = process_images(yes_images)
    no_inputs = process_images(no_images)
    end_time = time.time()
    
    execution_time = end_time - start_time
    print(f"Sequential execution time: {execution_time} seconds")

    return execution_time