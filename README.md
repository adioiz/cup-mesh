# Cup Contour Detection and Interpolation

This Python script expertly processes an image of a cup, employing advanced techniques to detect its edges and contours. Through a sophisticated series of steps, it minimizes the number of contour points for enhanced optimization and interpolates these points to forge a smooth outline of the cup. The script leverages the power of OpenCV for image processing, NumPy for high-level mathematical operations, matplotlib for comprehensive visualization, and SciPy for seamless contour interpolation.

## Key Features

- **Edge Detection**: Harnesses the Canny edge detector to accurately find edges within the cup image.
- **Contour Detection**: Efficiently identifies the cup's contours from the detected edges for further processing.
- **Contour Point Minimization**: Strategically reduces the points in detected contours, optimizing for a smoother interpolation process.
- **Spline Interpolation of Contours**: Applies spline interpolation to the refined contour points, producing a smooth and continuous curve that outlines the cup.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. This script has been tested with Python 3.8 and above. Additionally, the following packages need to be installed:

- OpenCV
- NumPy
- matplotlib
- SciPy

### Installation

First, clone this repository or download the script to your local machine. Then, navigate to the script's directory in your terminal and install the required Python packages using pip:

```bash
pip install -r requirements.txt
```
### Run script

```bash
python main.py
```


