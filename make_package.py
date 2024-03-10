import resume_edit as res
import cover_edit as cov

NAME = "Tianhao_Wang"

KNOWN_SKILLS = [
    "Agile Methodologies", "Scrum", "Software Development Life Cycle (SDLC)", "GitHub", "Perforce",
    "Continuous Integration", "Continuous Deployment", "CI/CD Pipelines",
    "Test Driven Development (TDD)", "Behavior Driven Development (BDD)", 
    "Unit Testing", "Integration Testing", "JUnit",
    "Mockito", "RESTful API", "Microservices Architecture",
    "Design Patterns", "Object-Oriented Programming (OOP)", "Functional Programming",
    "Database Management", "MySQL", "PostgreSQL", "Oracle SQL", "MongoDB",
    "Data Structures", "Algorithms", "System Design", 
    "Linux/Unix Administration", "Bash Scripting", "PowerShell", "Network Security", 
    "Cloud Computing", "Google Cloud Platform", "Kubernetes", "Vue.js", "Yarn",
    "User Testing", "Agile", "JIRA", "Confluence", "Client/Server", "Peer-to-Peer",
    "Data Visualization", "Google Charts", "CICD", "multi-treading",
    "Machine Learning", "TensorFlow", "PyTorch", "Data Analysis", "Pandas",
    "SQLAlchemy", "NumPy", "Matplotlib", "Data Cleaning", "Data Engineering",
    "Version Control Systems", "Software Debugging", "data migrations", "schema migrations", "maintaining databases",
    "Performance Optimization", "Distributed Systems", "Concurrency", "Parallel Computing", "Data Pipelines", "AI",
    "Game Development", "Mobile Application Development", "Android Development", "iOS Development", "Jenkins"
]
DEFAULT_SKILLS = {"ROS", "Git", "CMake", "Arduino", "Raspberry Pi", "Linux", "Valgrind", "GDB"}

def formatCompanyName(company_name: str) -> str:
    # Splits the name, capitalizes each part, and joins them back with underscores
    return '_'.join(word.capitalize() for word in company_name.split())

def getSkills(user_input: str) -> set[str]:
    if not user_input.strip():  # Check if the user input is empty
        return DEFAULT_SKILLS  # Return the default skills
    # Assume the user provides a multiline string of skills
    # Split this string into lines and create a set
    skills_set = set(user_input.strip().split('\n'))  # Split by new line
    return skills_set

def add_to_gitignore(formatted_company_name: str):
    # Define the path to your .gitignore file
    gitignore_path = '.gitignore'
    
    # Construct the new line to add to the .gitignore
    new_line = f"{formatted_company_name}/\n"
    
    # Open the .gitignore file and append the new line
    with open(gitignore_path, 'a') as file:
        file.write(new_line)


def main():
    # Ask user for the company's name
    company_name_input = input("Please enter the company's name: ")
    formatted_company_name = formatCompanyName(company_name_input)
    
    # Ask user for the skills text
    print("Please paste your skills text (leave empty to use default skills):")
    user_skills_text = ""
    while True:
        line = input()
        if line:
            user_skills_text += line + '\n'
        else:
            break

    # Process the skills text to extract relevant skills
    potential_skills = getSkills(user_skills_text)
    
    # Initialize an empty set for relevant skills
    relevant_skills = set()

    # Check if any known skills are in any part of the potential skills
    for known_skill in KNOWN_SKILLS:
        for potential_skill in potential_skills:
            # Convert both strings to lowercase for case-insensitive matching
            if known_skill.lower() in potential_skill.lower():
                relevant_skills.add(known_skill)
                break  # Stop looking once we've found the known skill in any potential skill
    
    print("Potential")
    print(potential_skills)
    print("--------")
    # Ensure default mandatory skills are included
    if(len(relevant_skills) > 0):
        relevant_skills.update({"Git", "Linux"})  # Add default tools that must be included
    else:
        relevant_skills = DEFAULT_SKILLS
    
    print(relevant_skills)
    print("--------")
    directory, resume = res.copy_and_rename_resume(NAME, formatted_company_name)
    res.add_skills(relevant_skills, directory, resume)

    cov.replace_company_name_in_docx(resume, formatted_company_name)
    res.compile_latex_to_pdf(directory, resume)
    add_to_gitignore(formatted_company_name)

# If this script is the main program being executed, call the main function
if __name__ == "__main__":
    main()
