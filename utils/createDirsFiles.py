import os
import csv

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
problemlist_path = os.path.join(project_root, 'problemList.csv')
problemrepo_path = os.path.join(project_root, 'ProblemRepo')
def create_problem_directories():
    # Path to the CSV file
    csv_file = problemlist_path
    
    # Read the CSV file
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if it exists
        
        for row in csv_reader:
            # Assuming the problem name is in the first column and link in the second
            problem_name = row[0]
            problem_link = row[1] if len(row) > 1 else "No link provided"
            
            # Create the directory path
            dir_path = os.path.join(problemrepo_path, problem_name)
            
            # Create the directory if it doesn't exist
            os.makedirs(dir_path, exist_ok=True)
            
            # Create question.txt file with the link
            with open(os.path.join(dir_path, 'question.txt'), 'w') as q_file:
                q_file.write(f"{problem_link}")
            
            # check if solution.py exists
            if not os.path.exists(os.path.join(dir_path, 'solution.py')):
                with open(os.path.join(dir_path, 'solution.py'), 'w') as s_file:
                    s_file.write(f"# Solution for {problem_name}")


    print("Directories and files created successfully.")
