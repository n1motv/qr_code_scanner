# QR Code Scanner

This Python script allows you to scan QR codes from an image file. It utilizes OpenCV for image processing and Pyzbar for decoding the QR code data. The script can detect multiple QR codes within a single image and display the decoded information along with a visual outline around each detected QR code.

## Features:

- **QR Code Detection**: Automatically detects and decodes multiple QR codes within a single image.
- **Data Extraction**: Extracts and prints the data encoded within the QR codes.
- **Visual Outline**: Draws a green outline around each detected QR code in the image.
- **Easy to Use**: Simple command-line interface for specifying the path to the image file.

## Prerequisites

Before using this script, ensure you have Python installed on your machine along with the necessary libraries. You can install the required libraries using pip:

```bash
pip install opencv-python pyzbar numpy
```

## How to Use:

1 - **Clone the Repository**: First, clone this repository to your local machine.

2 - **Install Dependencies**: Run the commands listed above under Prerequisites to install the necessary packages.

3 - **Running the Script**: Open your terminal, navigate to the script's directory, and use the following syntax to run the script:

```bash
python qr_code_scanner.py path_to_image_file
```

## Examples:

Scan a QR code from an image:

```bash
python qr_code_scanner.py "path/to/your/image.png"
```
After running the command, the script will display the decoded data and show the image with outlines around the detected QR codes.

## Contributions
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.
