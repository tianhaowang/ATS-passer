import subprocess
import os
import shutil

def copy_and_rename_resume(name: str, company: str) -> str:
    # Define the original file name and the new directory and file names
    original_file = "resume/resume.tex"
    new_dir = company
    file_name = f"{name}_{company}"
    new_file_path = os.path.join(new_dir, f"{file_name}_resume.tex")

    # Create the new directory if it doesn't already exist
    if(not os.path.exists(new_dir)):
        os.makedirs(new_dir, exist_ok=True)
    
    # Copy and rename the file
    if(not os.path.exists(new_file_path)):
        shutil.copy(original_file, new_file_path)
    
    # Verify that the file was copied and renamed
    if os.path.exists(new_file_path):
        print(f"File copied and renamed successfully: {new_file_path}")
        return new_dir, file_name
    else:
        print("Failed to copy and rename the file.")
        return "", ""

def add_skills(skills: list[str], directory: str, resume: str) -> bool:
    filename = f"{resume}_resume.tex"
    file_path = os.path.join(directory, filename)

    # Read the content of the file
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Flag to check if the line was found and modified
        modified = False

        # New skills string to be inserted
        new_skills = ', '.join(skills)

        # Go through each line to find the specific line
        for i, line in enumerate(lines):
            if r'\resumeSubItem{Addtional Skills}{}' in line:
                # Replace the empty {} with the skills from the list
                lines[i] = line.replace(r'{}', f'{{{new_skills}}}')
                modified = True
                break  # Assuming there's only one such line
        
        # Write back the modified content if any modification was made
        if modified:
            with open(file_path, 'w') as file:
                file.writelines(lines)
            return True  # The file was successfully modified
        else:
            return False  # The specific line was not found in the file
    except Exception as e:
        print(f"An error occurred: {e}")
        return False  # An error occurred during the process



def compile_latex_to_pdf(directory: str, file_name: str) -> str:
    # Define the directory and file names
    tex_file = f"{file_name}_resume.tex"
    pdf_file = f"{file_name}_resume.pdf"
    
    # Change to the directory where the .tex file is located
    os.chdir(directory)
    
    # Compile the LaTeX file into a PDF
    subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_file], check=True)
    
    # Change back to the original directory if needed
    # os.chdir(original_directory)
    
    # Check if the PDF was created
    if os.path.exists(pdf_file):
        print(f"PDF created successfully: {pdf_file}")
        return pdf_file
    else:
        print("Failed to create PDF.")
        return ""
