from PyPDF2 import PdfReader
import pyttsx3


pdf_path = "test.pdf"

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf = PdfReader(pdf_path)
        text = ''
        for page in range(len(pdf.pages)):
            page_text = pdf.pages[page].extract_text()
            text += page_text + ''
        return text

def convert_text_to_speech(text, output_file):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the speech rate (optional)
    engine.setProperty('volume', 1.0)  # Adjust the speech volume (optional)
    engine.save_to_file(text, output_file)
    engine.say(text)
    engine.runAndWait()


def main():
    pdf_path = 'test.pdf'
    output_file_name = input("save file as?")
    output_file = f"{output_file_name}.mp3"
    extract_text = extract_text_from_pdf(pdf_path)
    convert_text_to_speech(extract_text, output_file)

    print(f"Conversion completed audio saved as {output_file}")

if __name__ == "__main__":
    main()
