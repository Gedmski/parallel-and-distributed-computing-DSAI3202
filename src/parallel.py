import multiprocessing as mp
from tqdm import tqdm
from skimage.filters.rank import entropy
from skimage.morphology import disk
from scipy import ndimage as nd
from skimage.filters import sobel, gabor, hessian, prewitt

# Function to apply all filters to a single image
def process_single_image(image):
    return {
        'Original': image,
        'Entropy': entropy(image, disk(2)),
        'Gaussian': nd.gaussian_filter(image, sigma=1),
        'Sobel': sobel(image),
        'Gabor': gabor(image, frequency=0.9)[1],
        'Hessian': hessian(image, sigmas=range(1, 100, 1)),
        'Prewitt': prewitt(image)
    }

# Function to process images in parallel
def process_images_parallel(images, num_workers=mp.cpu_count()):
    with mp.Pool(processes=num_workers) as pool:
        processed_images = list(tqdm(pool.imap(process_single_image, images[:]), total=len(images[:])))
    return processed_images


def execution(yes_images, no_images):
    start_time = time.time()
    yes_inputs = process_images_parallel(yes_images)
    no_inputs = process_images_parallel(no_images)
    end_time = time.time()
    
    execution_time_p = end_time - start_time
    print(f"Parallel execution time: {execution_time_p:.2f} seconds")

    return execution_time_p, yes_inputs, no_inputs