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
    git clone https://github.com/shashank-vaidya/Data_extraction_via_OCR.git
    cd Data_extraction_via_OCR
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place the image from which you want to extract text in the repository directory. Update the `image_path` variable in the script with the name of your image file.

2. Run the script:
    ```bash
    python main.py
    ```

3. The extracted text will be saved in `output.json`, and the annotated image will be displayed.


### Main Function

1. Loads the image.
2. Extracts text using PaddleOCR.
3. Parses the OCR results.
4. Saves the extracted text to `output.json`.
5. Annotates the image with the extracted text and displays it using Matplotlib.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
