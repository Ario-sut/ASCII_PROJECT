# ASCII Art Converter

This Python script converts an image into ASCII art. It reads an image file, applies thresholding to convert it into grayscale, and maps the pixel values to ASCII symbols. The resulting ASCII art is printed to the console. The script performs the following steps:

1. Define a list of ASCII symbols and a list of thresholding values. These lists determine the symbol used to represent different intensity levels in the image.

2. Define the `print_out_ascii` function, which takes an array of ASCII codes and prints the corresponding ASCII symbols to the console.

3. Define the `image_to_ascii` function, which takes an image as input and converts it to ASCII format. This function resizes the image, applies thresholding, and returns the thresholded image as an array of ASCII codes.

4. In the main block (`if __name__ == "__main__":`), the script reads the image file specified in the command-line arguments. If no image path is provided, it uses a default image.

5. The `image_to_ascii` function is called to convert the image to ASCII format.

6. The `print_out_ascii` function is called to print the ASCII art to the console.

## Prerequisites

Before running the script, make sure you have the following packages installed:

- **OpenCV**: The OpenCV library is used for image processing.
- **NumPy**: The NumPy library is used for numerical operations.
- **Sys**: The Sys module provides access to command-line arguments.
  
▶️Please note that you need to have the required packages installed (OpenCV and NumPy) to run this script successfully. You can install them using the following command:


```shell
pip install opencv-python numpy

```shell
pip install opencv-python numpy
