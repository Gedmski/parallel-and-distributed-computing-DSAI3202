## The Code exemple
import numpy as np
import pandas as pd
import skimage.feature as feature

## Add your code here
manager = mp.Manager()
shared_list = manager.list()

# Function to compute GLCM features for an image
def compute_glcm_features(image, 
                                                    filter_name):
    """
    Computes GLCM (Gray Level Co-occurrence Matrix) features for an image.

    Parameters:
    - image: A 2D array representing the image. Should be in grayscale.
    - filter_name: A string representing the name of the filter applied to the image.

    Returns:
    - features: A dictionary containing the computed GLCM features. The keys are
        formatted as "{filter_name}_{feature_name}_{angle_index}", where "angle_index"
        corresponds to the index of the angle used for the GLCM calculation (1-based).
        The features include contrast, dissimilarity, homogeneity, energy, correlation,
        and ASM (Angular Second Moment) for each angle (0, π/4, π/2, 3π/4).

    Notes:
    - The image is first converted from float to uint8 format, as the graycomatrix
        function expects integer values.
    - The GLCM is computed using four angles (0, π/4, π/2, 3π/4) with a distance of 1.
    - The GLCM properties are computed and flattened into a 1D array to handle multiple
        angles. Each property value for each angle is stored as a separate key in the
        resulting dictionary.
    """
    # Convert the image from float to int
    image = (image * 255).astype(np.uint8)

    # Compute the GLCM
    graycom = feature.graycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)

    # Compute GLCM properties
    features = {}
    for prop in ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']:
            values = feature.graycoprops(graycom, prop).flatten()
            for i, value in enumerate(values):
                    features[f'{filter_name}_{prop}_{i+1}'] = value
    return features

# Decompose process by processing only one image at a time
def process_single_image(filtered_images, tumor_presence, shared_list):
    glcm_features = {}
    for key, image in filtered_images.items():
        glcm_features.update(compute_glcm_features(image, key))
    glcm_features['Tumor'] = tumor_presence
    shared_list.append(glcm_features)

# Process both inputs at the same time
def process_images_parallel(yes_inputs, no_inputs):
    # Create a process pool
    with mp.Pool(processes=mp.cpu_count()) as pool:
        tasks = [(img, 1, shared_list) for img in yes_inputs] + [(img, 0, shared_list) for img in no_inputs]
        pool.starmap(process_single_image, tasks)
        results = list(shared_list)
    return results

def execution(yes_inputs, no_inputs):
    start_time = time.time()  # Start timing
    
    glcm_features_list = process_images_parallel(yes_inputs, no_inputs)
    
    # Convert to DataFrame
    df = pd.DataFrame(glcm_features_list)
    print(df.head())
    
    end_time = time.time()  # End timing
    parallel_time = end_time - start_time
    print(f"Parallel Execution Time: {parallel_time:.2f} seconds")

    return df