# Author: Rafael Toppis
# Version: 1.0.0
# Date: 06.05.2024

import os
import PyPDF2
import logging
import glob as g

# Configurando o logger
logging.basicConfig(filename='processing.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def extract_text_from_pdf(pdf_file_path, output_file_path):
    text = ''
    success_message = f"{os.path.basename(pdf_file_path)} - success"
    
    # Open the PDF file
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
       
        # Iterate through each page and extract text
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            extracting = page.extract_text()
            # Try to concatenate the text
            try:
                text += extracting
            except Exception as e:
                # Log the error
                error_message = f"{os.path.basename(pdf_file_path)} - {e}"
                logging.error(error_message)
                return error_message
           
        # Save extracted text to a text file
        with open(output_file_path, 'w', encoding='utf-8', errors='ignore') as output_file:
            output_file.write(text)
               
        # Log success
        logging.info(success_message)
        return success_message


if __name__ == "__main__":
    # Provide the path to the PDF file and the output folder
    inputpath = "native"
    exportpath = "extracted_text"

    # Find all PDF files in the input directory
    pdf_files = g.glob(os.path.join(inputpath, "*.pdf"))

    # Process each PDF file
    for pdf_file in pdf_files:
        print("Loading File -> %s" % (pdf_file))
        filename = os.path.basename(pdf_file).replace(".pdf", ".txt").replace(".PDF", ".txt")
        output = os.path.join(exportpath, filename)
        
        # Attempt to extract text and log success or failure
        result = extract_text_from_pdf(pdf_file, output)
        if "success" in result:
            print(result)
        else:
            print(f"Error: {result}")