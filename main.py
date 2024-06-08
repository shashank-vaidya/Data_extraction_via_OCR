import json
import cv2
from paddleocr import PaddleOCR, draw_ocr
import matplotlib.pyplot as plt

def load_image(image_path):
    image = cv2.imread(image_path)
    return image

def extract_text(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Initialize PaddleOCR
    result = ocr.ocr(image_path, cls=True)  # Perform OCR
    return result

def parse_results(result):
    extracted_data = []
    for line in result:
        for word_info in line:
            word, confidence = word_info[1][0], word_info[1][1]
            coordinates = word_info[0]
            x1, y1 = int(coordinates[0][0]), int(coordinates[0][1])
            x2, y2 = int(coordinates[2][0]), int(coordinates[2][1])
            text_data = {
                'text': word,
                'confidence': confidence,
                'position': {
                    'left': x1,
                    'top': y1,
                    'width': x2 - x1,
                    'height': y2 - y1
                }
            }
            extracted_data.append(text_data)
    return extracted_data

def annotate_image(image, result):
    for line in result:
        for word_info in line:
            coordinates = word_info[0]
            x1, y1 = int(coordinates[0][0]), int(coordinates[0][1])
            x2, y2 = int(coordinates[2][0]), int(coordinates[2][1])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, word_info[1][0], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image

if __name__ == "__main__":
    image_path = 'Genova.png'  # Update the image path if needed
    image = load_image(image_path)
    result = extract_text(image_path)
    extracted_data = parse_results(result)

    with open('output.json', 'w') as outfile:
        json.dump(extracted_data, outfile, indent=4)

    annotated_image = annotate_image(image, result)

    plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
