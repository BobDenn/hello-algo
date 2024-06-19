import os


def find_tesseract():
    possible_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        r"C:\Tesseract-OCR\tesseract.exe"
    ]
    
    for path in possible_paths:
        if os.path.isfile(path):
            return path
    return None

tesseract_path = find_tesseract()
if tesseract_path:
    print(f"Tesseract found at: {tesseract_path}")
else:
    print("Tesseract not found. Please check your installation.")
    