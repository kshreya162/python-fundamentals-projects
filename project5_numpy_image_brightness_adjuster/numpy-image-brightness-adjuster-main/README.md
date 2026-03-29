# Image Brightness Adjuster using NumPy

This project demonstrates how NumPy arrays can be used to simulate basic image processing operations such as increasing and decreasing brightness.

In grayscale images, each pixel is represented by an integer value between 0 and 255:
- 0 → black
- 255 → white

The project creates a random grayscale image using NumPy and adjusts brightness using mathematical operations.



## Concepts Used

- NumPy arrays (2D arrays)
- Random number generation
- Arithmetic operations on arrays
- Broadcasting
- Value clipping using `np.clip()`

## Features

1. Creates a 5 × 5 grayscale image using NumPy
2. Increases brightness of the image
3. Decreases brightness of the image
4. Ensures pixel values remain between 0 and 255
5. Displays original, brighter, and darker images
