import os
import shutil
from docx import Document

def replace_company_name_in_docx(resume: str, company_name: str) -> bool:
    # Define the original and new file paths
    original_file = "cover/cover.docx"
    new_file_name = f"{resume}_{company_name}_Cover.docx"  # Assuming .docx since we're using python-docx
    new_file_path = os.path.join(company_name, new_file_name)

    # Ensure the destination directory exists
    os.makedirs(company_name, exist_ok=True)
    
    # Copy the original .doc file to the new destination as a .docx file
    shutil.copy(original_file, new_file_path)

    # Load the copied Word document for modification
    doc = Document(new_file_path)  # python-docx operates on .docx files
    
    # Replace {[Company Name]} with the actual company name in the whole document
    for paragraph in doc.paragraphs:
        if '{[Company Name]}' in paragraph.text:
            paragraph.text = paragraph.text.replace('{[Company Name]}', company_name)
    
    # Save the modified document as a Word file
    if doc.save(new_file_path):
        return True
    
    return False
