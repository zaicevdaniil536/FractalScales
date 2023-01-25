import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_scales():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    scales = f.generate()
    # Add noise to the fractal shape to make it look more like scales
    noise = np.random.normal(0, 0.05, scales.shape)
    scales = scales + noise
    scales = np.clip(scales, 0, 1)
    # Apply a scales-like color map to the fractal shape
    scales = plt.cm.Greens(scales)
    # Return the fractal scales
    return scales

# Generate 10 fractal scales images
for i in range(10):
    scales = generate_fractal_scales()
    plt.imsave("fractal_scales_{}.png".format(i), scales)
