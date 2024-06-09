# Image Text Extraction and Annotation

This repository contains a Python script to extract text from an image using PaddleOCR and annotate the image with the extracted text. The extracted text is saved in a JSON file.

## Requirements

- Python 3.x
- OpenCV
- PaddleOCR
- Matplotlib

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python-headless paddleocr matplotlib
    ```

## Usage

1. Place the image from which you want to extract text in the repository directory. Update the `image_path` variable in the script with the name of your image file.

2. Run the script:
    ```bash
    python script_name.py
    ```

3. The extracted text will be saved in `output.json`, and the annotated image will be displayed.

## Script Breakdown

### `load_image(image_path)`

Loads an image from the specified path using OpenCV.

### `extract_text(image_path)`

Uses PaddleOCR to perform OCR on the image and extract text.

### `parse_results(result)`

Parses the OCR results to extract text, confidence levels, and position coordinates. Formats the extracted data into a dictionary.

### `annotate_image(image, result)`

Annotates the original image with rectangles around detected text and overlays the extracted text on the image.

### Main Function

1. Loads the image.
2. Extracts text using PaddleOCR.
3. Parses the OCR results.
4. Saves the extracted text to `output.json`.
5. Annotates the image with the extracted text and displays it using Matplotlib.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```